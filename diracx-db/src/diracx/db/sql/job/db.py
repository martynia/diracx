from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

from sqlalchemy import bindparam, case, delete, func, insert, select, update
from sqlalchemy.exc import IntegrityError, NoResultFound

if TYPE_CHECKING:
    from sqlalchemy.sql.elements import BindParameter

from diracx.core.exceptions import InvalidQueryError, JobNotFoundError
from diracx.core.models import (
    LimitedJobStatusReturn,
    SearchSpec,
    SortSpec,
)

from ..utils import BaseSQLDB, apply_search_filters, apply_sort_constraints, get_columns
from .schema import (
    InputData,
    JobCommands,
    JobDBBase,
    JobJDLs,
    Jobs,
)


class JobDB(BaseSQLDB):
    metadata = JobDBBase.metadata

    # TODO: this is copied from the DIRAC JobDB
    # but is overwriten in LHCbDIRAC, so we need
    # to find a way to make it dynamic
    jdl_2_db_parameters = ["JobName", "JobType", "JobGroup"]

    async def summary(self, group_by, search) -> list[dict[str, str | int]]:
        columns = get_columns(Jobs.__table__, group_by)

        stmt = select(*columns, func.count(Jobs.job_id).label("count"))
        stmt = apply_search_filters(Jobs.__table__.columns.__getitem__, stmt, search)
        stmt = stmt.group_by(*columns)

        # Execute the query
        return [
            dict(row._mapping)
            async for row in (await self.conn.stream(stmt))
            if row.count > 0  # type: ignore
        ]

    async def search(
        self,
        parameters: list[str] | None,
        search: list[SearchSpec],
        sorts: list[SortSpec],
        *,
        distinct: bool = False,
        per_page: int = 100,
        page: int | None = None,
    ) -> tuple[int, list[dict[Any, Any]]]:
        # Find which columns to select
        columns = get_columns(Jobs.__table__, parameters)

        stmt = select(*columns)

        stmt = apply_search_filters(Jobs.__table__.columns.__getitem__, stmt, search)
        stmt = apply_sort_constraints(Jobs.__table__.columns.__getitem__, stmt, sorts)

        if distinct:
            stmt = stmt.distinct()

        # Calculate total count before applying pagination
        total_count_subquery = stmt.alias()
        total_count_stmt = select(func.count()).select_from(total_count_subquery)
        total = (await self.conn.execute(total_count_stmt)).scalar_one()

        # Apply pagination
        if page is not None:
            if page < 1:
                raise InvalidQueryError("Page must be a positive integer")
            if per_page < 1:
                raise InvalidQueryError("Per page must be a positive integer")
            stmt = stmt.offset((page - 1) * per_page).limit(per_page)

        # Execute the query
        return total, [
            dict(row._mapping) async for row in (await self.conn.stream(stmt))
        ]

    async def insert_input_data(self, lfns: dict[int, list[str]]):
        await self.conn.execute(
            InputData.__table__.insert(),
            [
                {
                    "JobID": job_id,
                    "LFN": lfn,
                }
                for job_id, lfns_ in lfns.items()
                for lfn in lfns_
            ],
        )

    async def set_job_attributes(self, job_id, job_data):
        """TODO: add myDate and force parameters."""
        if "Status" in job_data:
            job_data = job_data | {"LastUpdateTime": datetime.now(tz=timezone.utc)}
        stmt = update(Jobs).where(Jobs.job_id == job_id).values(job_data)
        await self.conn.execute(stmt)

    async def create_job(self, original_jdl):
        """Used to insert a new job with original JDL. Returns inserted job id."""
        from DIRAC.WorkloadManagementSystem.DB.JobDBUtils import compressJDL

        result = await self.conn.execute(
            JobJDLs.__table__.insert().values(
                JDL="",
                JobRequirements="",
                OriginalJDL=compressJDL(original_jdl),
            )
        )
        return result.lastrowid

    async def insert_job_attributes(self, jobs_to_update: dict[int, dict]):
        await self.conn.execute(
            Jobs.__table__.insert(),
            [
                {
                    "JobID": job_id,
                    **attrs,
                }
                for job_id, attrs in jobs_to_update.items()
            ],
        )

    async def update_job_jdls(self, jdls_to_update: dict[int, str]):
        """Used to update the JDL, typically just after inserting the original JDL, or rescheduling, for example."""
        from DIRAC.WorkloadManagementSystem.DB.JobDBUtils import compressJDL

        await self.conn.execute(
            JobJDLs.__table__.update().where(
                JobJDLs.__table__.c.JobID == bindparam("b_JobID")
            ),
            [
                {
                    "b_JobID": job_id,
                    "JDL": compressJDL(jdl),
                }
                for job_id, jdl in jdls_to_update.items()
            ],
        )

    async def check_and_prepare_job(
        self,
        job_id,
        class_ad_job,
        class_ad_req,
        owner,
        owner_group,
        job_attrs,
        vo,
    ):
        """Check Consistency of Submitted JDL and set some defaults
        Prepare subJDL with Job Requirements.
        """
        from DIRAC.Core.Utilities.DErrno import EWMSSUBM, cmpError
        from DIRAC.Core.Utilities.ReturnValues import returnValueOrRaise
        from DIRAC.WorkloadManagementSystem.DB.JobDBUtils import (
            checkAndPrepareJob,
        )

        ret_val = checkAndPrepareJob(
            job_id,
            class_ad_job,
            class_ad_req,
            owner,
            owner_group,
            job_attrs,
            vo,
        )

        if not ret_val["OK"]:
            if cmpError(ret_val, EWMSSUBM):
                await self.set_job_attributes(job_id, job_attrs)

            returnValueOrRaise(ret_val)

    async def set_job_jdl(self, job_id, jdl):
        from DIRAC.WorkloadManagementSystem.DB.JobDBUtils import compressJDL

        stmt = (
            update(JobJDLs).where(JobJDLs.job_id == job_id).values(JDL=compressJDL(jdl))
        )
        await self.conn.execute(stmt)

    async def set_job_jdl_bulk(self, jdls):
        from DIRAC.WorkloadManagementSystem.DB.JobDBUtils import compressJDL

        await self.conn.execute(
            JobJDLs.__table__.update().where(
                JobJDLs.__table__.c.JobID == bindparam("b_JobID")
            ),
            [{"b_JobID": jid, "JDL": compressJDL(jdl)} for jid, jdl in jdls.items()],
        )

    async def set_job_attributes_bulk(self, job_data):
        """TODO: add myDate and force parameters."""
        for job_id in job_data.keys():
            if "Status" in job_data[job_id]:
                job_data[job_id].update(
                    {"LastUpdateTime": datetime.now(tz=timezone.utc)}
                )
        columns = set(key for attrs in job_data.values() for key in attrs.keys())
        case_expressions = {
            column: case(
                *[
                    (Jobs.__table__.c.JobID == job_id, attrs[column])
                    for job_id, attrs in job_data.items()
                    if column in attrs
                ],
                else_=getattr(Jobs.__table__.c, column),  # Retain original value
            )
            for column in columns
        }

        stmt = (
            Jobs.__table__.update()
            .values(**case_expressions)
            .where(Jobs.__table__.c.JobID.in_(job_data.keys()))
        )
        await self.conn.execute(stmt)

    async def get_job_jdls(
        self, job_ids, original: bool = False
    ) -> dict[int | str, str]:
        from DIRAC.WorkloadManagementSystem.DB.JobDBUtils import extractJDL

        if original:
            stmt = select(JobJDLs.job_id, JobJDLs.original_jdl).where(
                JobJDLs.job_id.in_(job_ids)
            )
        else:
            stmt = select(JobJDLs.job_id, JobJDLs.jdl).where(
                JobJDLs.job_id.in_(job_ids)
            )

        return {
            jobid: extractJDL(jdl)
            for jobid, jdl in (await self.conn.execute(stmt))
            if jdl
        }

    async def get_job_status(self, job_id: int) -> LimitedJobStatusReturn:
        try:
            stmt = select(
                Jobs.status, Jobs.minor_status, Jobs.application_status
            ).where(Jobs.job_id == job_id)
            return LimitedJobStatusReturn(
                **dict((await self.conn.execute(stmt)).one()._mapping)
            )
        except NoResultFound as e:
            raise JobNotFoundError(job_id) from e

    async def set_job_command(self, job_id: int, command: str, arguments: str = ""):
        """Store a command to be passed to the job together with the next heart beat."""
        try:
            stmt = insert(JobCommands).values(
                JobID=job_id,
                Command=command,
                Arguments=arguments,
                ReceptionTime=datetime.now(tz=timezone.utc),
            )
            await self.conn.execute(stmt)
        except IntegrityError as e:
            raise JobNotFoundError(job_id) from e

    async def set_job_command_bulk(self, commands):
        """Store a command to be passed to the job together with the next heart beat."""
        await self.conn.execute(
            insert(JobCommands),
            [
                {
                    "JobID": job_id,
                    "Command": command,
                    "Arguments": arguments,
                    "ReceptionTime": datetime.now(tz=timezone.utc),
                }
                for job_id, command, arguments in commands
            ],
        )
        # FIXME handle IntegrityError

    async def delete_jobs(self, job_ids: list[int]):
        """Delete jobs from the database."""
        stmt = delete(JobJDLs).where(JobJDLs.job_id.in_(job_ids))
        await self.conn.execute(stmt)

    async def set_properties(
        self, properties: dict[int, dict[str, Any]], update_timestamp: bool = False
    ) -> int:
        """Update the job parameters
        All the jobs must update the same properties.

        :param properties: {job_id : {prop1: val1, prop2:val2}
        :param update_timestamp: if True, update the LastUpdate to now

        :return rowcount

        """
        # Check that all we always update the same set of properties
        required_parameters_set = {tuple(sorted(k.keys())) for k in properties.values()}

        if len(required_parameters_set) != 1:
            raise NotImplementedError(
                "All the jobs should update the same set of properties"
            )

        required_parameters = list(required_parameters_set)[0]
        update_parameters = [{"job_id": k, **v} for k, v in properties.items()]

        columns = get_columns(Jobs.__table__, required_parameters)
        values: dict[str, BindParameter[Any] | datetime] = {
            c.name: bindparam(c.name) for c in columns
        }
        if update_timestamp:
            values["LastUpdateTime"] = datetime.now(tz=timezone.utc)

        stmt = update(Jobs).where(Jobs.job_id == bindparam("job_id")).values(**values)
        rows = await self.conn.execute(stmt, update_parameters)

        return rows.rowcount
