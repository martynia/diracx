"""
Just repeat the diracx tests to make sure they still pass
"""

import pytest
from diracx.core.models import JobStatus
from fastapi.testclient import TestClient

pytestmark = pytest.mark.enabled_dependencies(
    [
        "AuthSettings",
        # CAUTION !!!
        # You need to put both the original AND your extended one
        "JobDB",
        "GubbinsJobDB",
        #######
        "JobLoggingDB",
        "WMSAccessPolicy",
        "ConfigSource",
        "TaskQueueDB",
        "DevelopmentSettings",
    ]
)


TEST_JDL = """
    Arguments = "jobDescription.xml -o LogLevel=INFO";
    Executable = "dirac-jobexec";
    JobGroup = jobGroup;
    JobName = jobName;
    JobType = User;
    LogLevel = INFO;
    OutputSandbox =
        {
            Script1_CodeOutput.log,
            std.err,
            std.out
        };
    Priority = 1;
    Site = ANY;
    StdError = std.err;
    StdOutput = std.out;
"""


@pytest.fixture
def normal_user_client(client_factory):
    with client_factory.normal_user() as client:
        yield client


@pytest.fixture
def valid_job_id(normal_user_client: TestClient):
    """
    Copied from the vanila tests
    This ensures that the submission route works

    """
    job_definitions = [TEST_JDL]
    r = normal_user_client.post("/api/jobs/", json=job_definitions)
    assert r.status_code == 200, r.json()
    assert len(r.json()) == 1
    return r.json()[0]["JobID"]


def test_gubbins_job_router(normal_user_client, valid_job_id):
    """
    Basically like diracx test_delete_job_valid_job_id
    except that the job does not go into DELETED status,
    as the method is intercepted by the DB
    """

    # We search for the job
    r = normal_user_client.get(f"/api/jobs/{valid_job_id}/status")
    assert r.status_code == 200, r.json()
    assert r.json()[str(valid_job_id)]["Status"] == JobStatus.RECEIVED

    # We delete the job, and here we expect that nothing
    # actually happened
    r = normal_user_client.delete(f"/api/jobs/{valid_job_id}")
    assert r.status_code == 200, r.json()

    r = normal_user_client.get(f"/api/jobs/{valid_job_id}/status")
    assert r.status_code == 200, r.json()
    # The job would normally be deleted
    assert r.json()[str(valid_job_id)]["Status"] == JobStatus.RECEIVED