# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.3, generator: @autorest/python@6.27.1)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
import sys
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore

if TYPE_CHECKING:
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class BodyAuthToken(_serialization.Model):
    """Body_auth_token.

    All required parameters must be populated in order to send to server.

    :ivar grant_type: OAuth2 Grant type. Required.
    :vartype grant_type: ~generated.models.BodyAuthTokenGrantType
    :ivar client_id: OAuth2 client id. Required.
    :vartype client_id: str
    :ivar device_code: device code for OAuth2 device flow.
    :vartype device_code: str
    :ivar code: Code for OAuth2 authorization code flow.
    :vartype code: str
    :ivar redirect_uri: redirect_uri used with OAuth2 authorization code flow.
    :vartype redirect_uri: str
    :ivar code_verifier: Verifier for the code challenge for the OAuth2 authorization flow with
     PKCE.
    :vartype code_verifier: str
    :ivar refresh_token: Refresh token used with OAuth2 refresh token flow.
    :vartype refresh_token: str
    """

    _validation = {
        "grant_type": {"required": True},
        "client_id": {"required": True},
    }

    _attribute_map = {
        "grant_type": {"key": "grant_type", "type": "BodyAuthTokenGrantType"},
        "client_id": {"key": "client_id", "type": "str"},
        "device_code": {"key": "device_code", "type": "str"},
        "code": {"key": "code", "type": "str"},
        "redirect_uri": {"key": "redirect_uri", "type": "str"},
        "code_verifier": {"key": "code_verifier", "type": "str"},
        "refresh_token": {"key": "refresh_token", "type": "str"},
    }

    def __init__(
        self,
        *,
        grant_type: "_models.BodyAuthTokenGrantType",
        client_id: str,
        device_code: Optional[str] = None,
        code: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        code_verifier: Optional[str] = None,
        refresh_token: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        :keyword grant_type: OAuth2 Grant type. Required.
        :paramtype grant_type: ~generated.models.BodyAuthTokenGrantType
        :keyword client_id: OAuth2 client id. Required.
        :paramtype client_id: str
        :keyword device_code: device code for OAuth2 device flow.
        :paramtype device_code: str
        :keyword code: Code for OAuth2 authorization code flow.
        :paramtype code: str
        :keyword redirect_uri: redirect_uri used with OAuth2 authorization code flow.
        :paramtype redirect_uri: str
        :keyword code_verifier: Verifier for the code challenge for the OAuth2 authorization flow with
         PKCE.
        :paramtype code_verifier: str
        :keyword refresh_token: Refresh token used with OAuth2 refresh token flow.
        :paramtype refresh_token: str
        """
        super().__init__(**kwargs)
        self.grant_type = grant_type
        self.client_id = client_id
        self.device_code = device_code
        self.code = code
        self.redirect_uri = redirect_uri
        self.code_verifier = code_verifier
        self.refresh_token = refresh_token


class BodyAuthTokenGrantType(_serialization.Model):
    """OAuth2 Grant type."""


class DevelopmentSettings(_serialization.Model):
    """Settings for the Development Configuration that can influence run time.

    :ivar crash_on_missed_access_policy: Crash On Missed Access Policy.
    :vartype crash_on_missed_access_policy: bool
    """

    _attribute_map = {
        "crash_on_missed_access_policy": {
            "key": "crash_on_missed_access_policy",
            "type": "bool",
        },
    }

    def __init__(
        self, *, crash_on_missed_access_policy: bool = False, **kwargs: Any
    ) -> None:
        """
        :keyword crash_on_missed_access_policy: Crash On Missed Access Policy.
        :paramtype crash_on_missed_access_policy: bool
        """
        super().__init__(**kwargs)
        self.crash_on_missed_access_policy = crash_on_missed_access_policy


class GroupInfo(_serialization.Model):
    """GroupInfo.

    All required parameters must be populated in order to send to server.

    :ivar properties: Properties. Required.
    :vartype properties: list[str]
    """

    _validation = {
        "properties": {"required": True},
    }

    _attribute_map = {
        "properties": {"key": "properties", "type": "[str]"},
    }

    def __init__(self, *, properties: List[str], **kwargs: Any) -> None:
        """
        :keyword properties: Properties. Required.
        :paramtype properties: list[str]
        """
        super().__init__(**kwargs)
        self.properties = properties


class HTTPValidationError(_serialization.Model):
    """HTTPValidationError.

    :ivar detail: Detail.
    :vartype detail: list[~generated.models.ValidationError]
    """

    _attribute_map = {
        "detail": {"key": "detail", "type": "[ValidationError]"},
    }

    def __init__(
        self, *, detail: Optional[List["_models.ValidationError"]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword detail: Detail.
        :paramtype detail: list[~generated.models.ValidationError]
        """
        super().__init__(**kwargs)
        self.detail = detail


class InitiateDeviceFlowResponse(_serialization.Model):
    """Response for the device flow initiation.

    All required parameters must be populated in order to send to server.

    :ivar user_code: User Code. Required.
    :vartype user_code: str
    :ivar device_code: Device Code. Required.
    :vartype device_code: str
    :ivar verification_uri_complete: Verification Uri Complete. Required.
    :vartype verification_uri_complete: str
    :ivar verification_uri: Verification Uri. Required.
    :vartype verification_uri: str
    :ivar expires_in: Expires In. Required.
    :vartype expires_in: int
    """

    _validation = {
        "user_code": {"required": True},
        "device_code": {"required": True},
        "verification_uri_complete": {"required": True},
        "verification_uri": {"required": True},
        "expires_in": {"required": True},
    }

    _attribute_map = {
        "user_code": {"key": "user_code", "type": "str"},
        "device_code": {"key": "device_code", "type": "str"},
        "verification_uri_complete": {
            "key": "verification_uri_complete",
            "type": "str",
        },
        "verification_uri": {"key": "verification_uri", "type": "str"},
        "expires_in": {"key": "expires_in", "type": "int"},
    }

    def __init__(
        self,
        *,
        user_code: str,
        device_code: str,
        verification_uri_complete: str,
        verification_uri: str,
        expires_in: int,
        **kwargs: Any,
    ) -> None:
        """
        :keyword user_code: User Code. Required.
        :paramtype user_code: str
        :keyword device_code: Device Code. Required.
        :paramtype device_code: str
        :keyword verification_uri_complete: Verification Uri Complete. Required.
        :paramtype verification_uri_complete: str
        :keyword verification_uri: Verification Uri. Required.
        :paramtype verification_uri: str
        :keyword expires_in: Expires In. Required.
        :paramtype expires_in: int
        """
        super().__init__(**kwargs)
        self.user_code = user_code
        self.device_code = device_code
        self.verification_uri_complete = verification_uri_complete
        self.verification_uri = verification_uri
        self.expires_in = expires_in


class InsertedJob(_serialization.Model):
    """InsertedJob.

    All required parameters must be populated in order to send to server.

    :ivar job_id: Jobid. Required.
    :vartype job_id: int
    :ivar status: Status. Required.
    :vartype status: str
    :ivar minor_status: Minorstatus. Required.
    :vartype minor_status: str
    :ivar time_stamp: Timestamp. Required.
    :vartype time_stamp: ~datetime.datetime
    """

    _validation = {
        "job_id": {"required": True},
        "status": {"required": True},
        "minor_status": {"required": True},
        "time_stamp": {"required": True},
    }

    _attribute_map = {
        "job_id": {"key": "JobID", "type": "int"},
        "status": {"key": "Status", "type": "str"},
        "minor_status": {"key": "MinorStatus", "type": "str"},
        "time_stamp": {"key": "TimeStamp", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        job_id: int,
        status: str,
        minor_status: str,
        time_stamp: datetime.datetime,
        **kwargs: Any,
    ) -> None:
        """
        :keyword job_id: Jobid. Required.
        :paramtype job_id: int
        :keyword status: Status. Required.
        :paramtype status: str
        :keyword minor_status: Minorstatus. Required.
        :paramtype minor_status: str
        :keyword time_stamp: Timestamp. Required.
        :paramtype time_stamp: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.job_id = job_id
        self.status = status
        self.minor_status = minor_status
        self.time_stamp = time_stamp


class JobSearchParams(_serialization.Model):
    """JobSearchParams.

    :ivar parameters: Parameters.
    :vartype parameters: list[str]
    :ivar search: Search.
    :vartype search: list[~generated.models.JobSearchParamsSearchItem]
    :ivar sort: Sort.
    :vartype sort: list[~generated.models.SortSpec]
    :ivar distinct: Distinct.
    :vartype distinct: bool
    """

    _attribute_map = {
        "parameters": {"key": "parameters", "type": "[str]"},
        "search": {"key": "search", "type": "[JobSearchParamsSearchItem]"},
        "sort": {"key": "sort", "type": "[SortSpec]"},
        "distinct": {"key": "distinct", "type": "bool"},
    }

    def __init__(
        self,
        *,
        parameters: Optional[List[str]] = None,
        search: List["_models.JobSearchParamsSearchItem"] = [],
        sort: List["_models.SortSpec"] = [],
        distinct: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        :keyword parameters: Parameters.
        :paramtype parameters: list[str]
        :keyword search: Search.
        :paramtype search: list[~generated.models.JobSearchParamsSearchItem]
        :keyword sort: Sort.
        :paramtype sort: list[~generated.models.SortSpec]
        :keyword distinct: Distinct.
        :paramtype distinct: bool
        """
        super().__init__(**kwargs)
        self.parameters = parameters
        self.search = search
        self.sort = sort
        self.distinct = distinct


class JobSearchParamsSearchItem(_serialization.Model):
    """JobSearchParamsSearchItem."""


class JobStatusUpdate(_serialization.Model):
    """JobStatusUpdate.

    :ivar status: JobStatus. Known values are: "Submitting", "Received", "Checking", "Staging",
     "Waiting", "Matched", "Running", "Stalled", "Completing", "Done", "Completed", "Failed",
     "Deleted", "Killed", and "Rescheduled".
    :vartype status: str or ~generated.models.JobStatus
    :ivar minor_status: Minorstatus.
    :vartype minor_status: str
    :ivar application_status: Applicationstatus.
    :vartype application_status: str
    :ivar source: Source.
    :vartype source: str
    """

    _attribute_map = {
        "status": {"key": "Status", "type": "str"},
        "minor_status": {"key": "MinorStatus", "type": "str"},
        "application_status": {"key": "ApplicationStatus", "type": "str"},
        "source": {"key": "Source", "type": "str"},
    }

    def __init__(
        self,
        *,
        status: Optional[Union[str, "_models.JobStatus"]] = None,
        minor_status: Optional[str] = None,
        application_status: Optional[str] = None,
        source: str = "Unknown",
        **kwargs: Any,
    ) -> None:
        """
        :keyword status: JobStatus. Known values are: "Submitting", "Received", "Checking", "Staging",
         "Waiting", "Matched", "Running", "Stalled", "Completing", "Done", "Completed", "Failed",
         "Deleted", "Killed", and "Rescheduled".
        :paramtype status: str or ~generated.models.JobStatus
        :keyword minor_status: Minorstatus.
        :paramtype minor_status: str
        :keyword application_status: Applicationstatus.
        :paramtype application_status: str
        :keyword source: Source.
        :paramtype source: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.minor_status = minor_status
        self.application_status = application_status
        self.source = source


class JobSummaryParams(_serialization.Model):
    """JobSummaryParams.

    All required parameters must be populated in order to send to server.

    :ivar grouping: Grouping. Required.
    :vartype grouping: list[str]
    :ivar search: Search.
    :vartype search: list[~generated.models.JobSummaryParamsSearchItem]
    """

    _validation = {
        "grouping": {"required": True},
    }

    _attribute_map = {
        "grouping": {"key": "grouping", "type": "[str]"},
        "search": {"key": "search", "type": "[JobSummaryParamsSearchItem]"},
    }

    def __init__(
        self,
        *,
        grouping: List[str],
        search: List["_models.JobSummaryParamsSearchItem"] = [],
        **kwargs: Any,
    ) -> None:
        """
        :keyword grouping: Grouping. Required.
        :paramtype grouping: list[str]
        :keyword search: Search.
        :paramtype search: list[~generated.models.JobSummaryParamsSearchItem]
        """
        super().__init__(**kwargs)
        self.grouping = grouping
        self.search = search


class JobSummaryParamsSearchItem(_serialization.Model):
    """JobSummaryParamsSearchItem."""


class Metadata(_serialization.Model):
    """Metadata.

    All required parameters must be populated in order to send to server.

    :ivar virtual_organizations: Virtual Organizations. Required.
    :vartype virtual_organizations: dict[str, ~generated.models.VOInfo]
    :ivar development_settings: Settings for the Development Configuration that can influence run
     time. Required.
    :vartype development_settings: ~generated.models.DevelopmentSettings
    """

    _validation = {
        "virtual_organizations": {"required": True},
        "development_settings": {"required": True},
    }

    _attribute_map = {
        "virtual_organizations": {"key": "virtual_organizations", "type": "{VOInfo}"},
        "development_settings": {
            "key": "development_settings",
            "type": "DevelopmentSettings",
        },
    }

    def __init__(
        self,
        *,
        virtual_organizations: Dict[str, "_models.VOInfo"],
        development_settings: "_models.DevelopmentSettings",
        **kwargs: Any,
    ) -> None:
        """
        :keyword virtual_organizations: Virtual Organizations. Required.
        :paramtype virtual_organizations: dict[str, ~generated.models.VOInfo]
        :keyword development_settings: Settings for the Development Configuration that can influence
         run time. Required.
        :paramtype development_settings: ~generated.models.DevelopmentSettings
        """
        super().__init__(**kwargs)
        self.virtual_organizations = virtual_organizations
        self.development_settings = development_settings


class SandboxDownloadResponse(_serialization.Model):
    """SandboxDownloadResponse.

    All required parameters must be populated in order to send to server.

    :ivar url: Url. Required.
    :vartype url: str
    :ivar expires_in: Expires In. Required.
    :vartype expires_in: int
    """

    _validation = {
        "url": {"required": True},
        "expires_in": {"required": True},
    }

    _attribute_map = {
        "url": {"key": "url", "type": "str"},
        "expires_in": {"key": "expires_in", "type": "int"},
    }

    def __init__(self, *, url: str, expires_in: int, **kwargs: Any) -> None:
        """
        :keyword url: Url. Required.
        :paramtype url: str
        :keyword expires_in: Expires In. Required.
        :paramtype expires_in: int
        """
        super().__init__(**kwargs)
        self.url = url
        self.expires_in = expires_in


class SandboxInfo(_serialization.Model):
    """SandboxInfo.

    All required parameters must be populated in order to send to server.

    :ivar checksum_algorithm: ChecksumAlgorithm. Required. "sha256"
    :vartype checksum_algorithm: str or ~generated.models.ChecksumAlgorithm
    :ivar checksum: Checksum. Required.
    :vartype checksum: str
    :ivar size: Size. Required.
    :vartype size: int
    :ivar format: SandboxFormat. Required. "tar.bz2"
    :vartype format: str or ~generated.models.SandboxFormat
    """

    _validation = {
        "checksum_algorithm": {"required": True},
        "checksum": {"required": True, "pattern": r"^[0-9a-fA-F]{64}$"},
        "size": {"required": True, "minimum": 1},
        "format": {"required": True},
    }

    _attribute_map = {
        "checksum_algorithm": {"key": "checksum_algorithm", "type": "str"},
        "checksum": {"key": "checksum", "type": "str"},
        "size": {"key": "size", "type": "int"},
        "format": {"key": "format", "type": "str"},
    }

    def __init__(
        self,
        *,
        checksum_algorithm: Union[str, "_models.ChecksumAlgorithm"],
        checksum: str,
        size: int,
        format: Union[str, "_models.SandboxFormat"],
        **kwargs: Any,
    ) -> None:
        """
        :keyword checksum_algorithm: ChecksumAlgorithm. Required. "sha256"
        :paramtype checksum_algorithm: str or ~generated.models.ChecksumAlgorithm
        :keyword checksum: Checksum. Required.
        :paramtype checksum: str
        :keyword size: Size. Required.
        :paramtype size: int
        :keyword format: SandboxFormat. Required. "tar.bz2"
        :paramtype format: str or ~generated.models.SandboxFormat
        """
        super().__init__(**kwargs)
        self.checksum_algorithm = checksum_algorithm
        self.checksum = checksum
        self.size = size
        self.format = format


class SandboxUploadResponse(_serialization.Model):
    """SandboxUploadResponse.

    All required parameters must be populated in order to send to server.

    :ivar pfn: Pfn. Required.
    :vartype pfn: str
    :ivar url: Url.
    :vartype url: str
    :ivar fields: Fields.
    :vartype fields: dict[str, str]
    """

    _validation = {
        "pfn": {"required": True},
    }

    _attribute_map = {
        "pfn": {"key": "pfn", "type": "str"},
        "url": {"key": "url", "type": "str"},
        "fields": {"key": "fields", "type": "{str}"},
    }

    def __init__(
        self,
        *,
        pfn: str,
        url: Optional[str] = None,
        fields: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> None:
        """
        :keyword pfn: Pfn. Required.
        :paramtype pfn: str
        :keyword url: Url.
        :paramtype url: str
        :keyword fields: Fields.
        :paramtype fields: dict[str, str]
        """
        super().__init__(**kwargs)
        self.pfn = pfn
        self.url = url
        self.fields = fields


class ScalarSearchSpec(_serialization.Model):
    """ScalarSearchSpec.

    All required parameters must be populated in order to send to server.

    :ivar parameter: Parameter. Required.
    :vartype parameter: str
    :ivar operator: ScalarSearchOperator. Required. Known values are: "eq", "neq", "gt", "lt", and
     "like".
    :vartype operator: str or ~generated.models.ScalarSearchOperator
    :ivar value: Value. Required.
    :vartype value: ~generated.models.ScalarSearchSpecValue
    """

    _validation = {
        "parameter": {"required": True},
        "operator": {"required": True},
        "value": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
        "operator": {"key": "operator", "type": "str"},
        "value": {"key": "value", "type": "ScalarSearchSpecValue"},
    }

    def __init__(
        self,
        *,
        parameter: str,
        operator: Union[str, "_models.ScalarSearchOperator"],
        value: "_models.ScalarSearchSpecValue",
        **kwargs: Any,
    ) -> None:
        """
        :keyword parameter: Parameter. Required.
        :paramtype parameter: str
        :keyword operator: ScalarSearchOperator. Required. Known values are: "eq", "neq", "gt", "lt",
         and "like".
        :paramtype operator: str or ~generated.models.ScalarSearchOperator
        :keyword value: Value. Required.
        :paramtype value: ~generated.models.ScalarSearchSpecValue
        """
        super().__init__(**kwargs)
        self.parameter = parameter
        self.operator = operator
        self.value = value


class ScalarSearchSpecValue(_serialization.Model):
    """Value."""


class SetJobStatusReturn(_serialization.Model):
    """SetJobStatusReturn.

    All required parameters must be populated in order to send to server.

    :ivar success: Success. Required.
    :vartype success: dict[str, ~generated.models.SetJobStatusReturnSuccess]
    :ivar failed: Failed. Required.
    :vartype failed: dict[str, dict[str, str]]
    """

    _validation = {
        "success": {"required": True},
        "failed": {"required": True},
    }

    _attribute_map = {
        "success": {"key": "success", "type": "{SetJobStatusReturnSuccess}"},
        "failed": {"key": "failed", "type": "{{str}}"},
    }

    def __init__(
        self,
        *,
        success: Dict[str, "_models.SetJobStatusReturnSuccess"],
        failed: Dict[str, Dict[str, str]],
        **kwargs: Any,
    ) -> None:
        """
        :keyword success: Success. Required.
        :paramtype success: dict[str, ~generated.models.SetJobStatusReturnSuccess]
        :keyword failed: Failed. Required.
        :paramtype failed: dict[str, dict[str, str]]
        """
        super().__init__(**kwargs)
        self.success = success
        self.failed = failed


class SetJobStatusReturnSuccess(_serialization.Model):
    """Successful new status change.

    :ivar status: JobStatus. Known values are: "Submitting", "Received", "Checking", "Staging",
     "Waiting", "Matched", "Running", "Stalled", "Completing", "Done", "Completed", "Failed",
     "Deleted", "Killed", and "Rescheduled".
    :vartype status: str or ~generated.models.JobStatus
    :ivar minor_status: Minorstatus.
    :vartype minor_status: str
    :ivar application_status: Applicationstatus.
    :vartype application_status: str
    :ivar heart_beat_time: Heartbeattime.
    :vartype heart_beat_time: ~datetime.datetime
    :ivar start_exec_time: Startexectime.
    :vartype start_exec_time: ~datetime.datetime
    :ivar end_exec_time: Endexectime.
    :vartype end_exec_time: ~datetime.datetime
    :ivar last_update_time: Lastupdatetime.
    :vartype last_update_time: ~datetime.datetime
    """

    _attribute_map = {
        "status": {"key": "Status", "type": "str"},
        "minor_status": {"key": "MinorStatus", "type": "str"},
        "application_status": {"key": "ApplicationStatus", "type": "str"},
        "heart_beat_time": {"key": "HeartBeatTime", "type": "iso-8601"},
        "start_exec_time": {"key": "StartExecTime", "type": "iso-8601"},
        "end_exec_time": {"key": "EndExecTime", "type": "iso-8601"},
        "last_update_time": {"key": "LastUpdateTime", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        status: Optional[Union[str, "_models.JobStatus"]] = None,
        minor_status: Optional[str] = None,
        application_status: Optional[str] = None,
        heart_beat_time: Optional[datetime.datetime] = None,
        start_exec_time: Optional[datetime.datetime] = None,
        end_exec_time: Optional[datetime.datetime] = None,
        last_update_time: Optional[datetime.datetime] = None,
        **kwargs: Any,
    ) -> None:
        """
        :keyword status: JobStatus. Known values are: "Submitting", "Received", "Checking", "Staging",
         "Waiting", "Matched", "Running", "Stalled", "Completing", "Done", "Completed", "Failed",
         "Deleted", "Killed", and "Rescheduled".
        :paramtype status: str or ~generated.models.JobStatus
        :keyword minor_status: Minorstatus.
        :paramtype minor_status: str
        :keyword application_status: Applicationstatus.
        :paramtype application_status: str
        :keyword heart_beat_time: Heartbeattime.
        :paramtype heart_beat_time: ~datetime.datetime
        :keyword start_exec_time: Startexectime.
        :paramtype start_exec_time: ~datetime.datetime
        :keyword end_exec_time: Endexectime.
        :paramtype end_exec_time: ~datetime.datetime
        :keyword last_update_time: Lastupdatetime.
        :paramtype last_update_time: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.status = status
        self.minor_status = minor_status
        self.application_status = application_status
        self.heart_beat_time = heart_beat_time
        self.start_exec_time = start_exec_time
        self.end_exec_time = end_exec_time
        self.last_update_time = last_update_time


class SortSpec(_serialization.Model):
    """SortSpec.

    All required parameters must be populated in order to send to server.

    :ivar parameter: Parameter. Required.
    :vartype parameter: str
    :ivar direction: SortDirection. Required. Known values are: "asc" and "desc".
    :vartype direction: str or ~generated.models.SortDirection
    """

    _validation = {
        "parameter": {"required": True},
        "direction": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
        "direction": {"key": "direction", "type": "str"},
    }

    def __init__(
        self,
        *,
        parameter: str,
        direction: Union[str, "_models.SortDirection"],
        **kwargs: Any,
    ) -> None:
        """
        :keyword parameter: Parameter. Required.
        :paramtype parameter: str
        :keyword direction: SortDirection. Required. Known values are: "asc" and "desc".
        :paramtype direction: str or ~generated.models.SortDirection
        """
        super().__init__(**kwargs)
        self.parameter = parameter
        self.direction = direction


class SupportInfo(_serialization.Model):
    """SupportInfo.

    All required parameters must be populated in order to send to server.

    :ivar message: Message. Required.
    :vartype message: str
    :ivar webpage: Webpage. Required.
    :vartype webpage: str
    :ivar email: Email. Required.
    :vartype email: str
    """

    _validation = {
        "message": {"required": True},
        "webpage": {"required": True},
        "email": {"required": True},
    }

    _attribute_map = {
        "message": {"key": "message", "type": "str"},
        "webpage": {"key": "webpage", "type": "str"},
        "email": {"key": "email", "type": "str"},
    }

    def __init__(
        self, *, message: str, webpage: str, email: str, **kwargs: Any
    ) -> None:
        """
        :keyword message: Message. Required.
        :paramtype message: str
        :keyword webpage: Webpage. Required.
        :paramtype webpage: str
        :keyword email: Email. Required.
        :paramtype email: str
        """
        super().__init__(**kwargs)
        self.message = message
        self.webpage = webpage
        self.email = email


class TokenResponse(_serialization.Model):
    """TokenResponse.

    All required parameters must be populated in order to send to server.

    :ivar access_token: Access Token. Required.
    :vartype access_token: str
    :ivar expires_in: Expires In. Required.
    :vartype expires_in: int
    :ivar token_type: Token Type.
    :vartype token_type: str
    :ivar refresh_token: Refresh Token.
    :vartype refresh_token: str
    """

    _validation = {
        "access_token": {"required": True},
        "expires_in": {"required": True},
    }

    _attribute_map = {
        "access_token": {"key": "access_token", "type": "str"},
        "expires_in": {"key": "expires_in", "type": "int"},
        "token_type": {"key": "token_type", "type": "str"},
        "refresh_token": {"key": "refresh_token", "type": "str"},
    }

    def __init__(
        self,
        *,
        access_token: str,
        expires_in: int,
        token_type: str = "Bearer",
        refresh_token: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """
        :keyword access_token: Access Token. Required.
        :paramtype access_token: str
        :keyword expires_in: Expires In. Required.
        :paramtype expires_in: int
        :keyword token_type: Token Type.
        :paramtype token_type: str
        :keyword refresh_token: Refresh Token.
        :paramtype refresh_token: str
        """
        super().__init__(**kwargs)
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.refresh_token = refresh_token


class UserInfoResponse(_serialization.Model):
    """Response for the userinfo endpoint.

    All required parameters must be populated in order to send to server.

    :ivar sub: Sub. Required.
    :vartype sub: str
    :ivar vo: Vo. Required.
    :vartype vo: str
    :ivar dirac_group: Dirac Group. Required.
    :vartype dirac_group: str
    :ivar policies: Policies. Required.
    :vartype policies: JSON
    :ivar properties: Properties. Required.
    :vartype properties: list[str]
    :ivar preferred_username: Preferred Username. Required.
    :vartype preferred_username: str
    """

    _validation = {
        "sub": {"required": True},
        "vo": {"required": True},
        "dirac_group": {"required": True},
        "policies": {"required": True},
        "properties": {"required": True},
        "preferred_username": {"required": True},
    }

    _attribute_map = {
        "sub": {"key": "sub", "type": "str"},
        "vo": {"key": "vo", "type": "str"},
        "dirac_group": {"key": "dirac_group", "type": "str"},
        "policies": {"key": "policies", "type": "object"},
        "properties": {"key": "properties", "type": "[str]"},
        "preferred_username": {"key": "preferred_username", "type": "str"},
    }

    def __init__(
        self,
        *,
        sub: str,
        vo: str,
        dirac_group: str,
        policies: JSON,
        properties: List[str],
        preferred_username: str,
        **kwargs: Any,
    ) -> None:
        """
        :keyword sub: Sub. Required.
        :paramtype sub: str
        :keyword vo: Vo. Required.
        :paramtype vo: str
        :keyword dirac_group: Dirac Group. Required.
        :paramtype dirac_group: str
        :keyword policies: Policies. Required.
        :paramtype policies: JSON
        :keyword properties: Properties. Required.
        :paramtype properties: list[str]
        :keyword preferred_username: Preferred Username. Required.
        :paramtype preferred_username: str
        """
        super().__init__(**kwargs)
        self.sub = sub
        self.vo = vo
        self.dirac_group = dirac_group
        self.policies = policies
        self.properties = properties
        self.preferred_username = preferred_username


class ValidationError(_serialization.Model):
    """ValidationError.

    All required parameters must be populated in order to send to server.

    :ivar loc: Location. Required.
    :vartype loc: list[~generated.models.ValidationErrorLocItem]
    :ivar msg: Message. Required.
    :vartype msg: str
    :ivar type: Error Type. Required.
    :vartype type: str
    """

    _validation = {
        "loc": {"required": True},
        "msg": {"required": True},
        "type": {"required": True},
    }

    _attribute_map = {
        "loc": {"key": "loc", "type": "[ValidationErrorLocItem]"},
        "msg": {"key": "msg", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(
        self,
        *,
        loc: List["_models.ValidationErrorLocItem"],
        msg: str,
        type: str,
        **kwargs: Any,
    ) -> None:
        """
        :keyword loc: Location. Required.
        :paramtype loc: list[~generated.models.ValidationErrorLocItem]
        :keyword msg: Message. Required.
        :paramtype msg: str
        :keyword type: Error Type. Required.
        :paramtype type: str
        """
        super().__init__(**kwargs)
        self.loc = loc
        self.msg = msg
        self.type = type


class ValidationErrorLocItem(_serialization.Model):
    """ValidationErrorLocItem."""


class VectorSearchSpec(_serialization.Model):
    """VectorSearchSpec.

    All required parameters must be populated in order to send to server.

    :ivar parameter: Parameter. Required.
    :vartype parameter: str
    :ivar operator: VectorSearchOperator. Required. Known values are: "in" and "not in".
    :vartype operator: str or ~generated.models.VectorSearchOperator
    :ivar values: Values. Required.
    :vartype values: ~generated.models.VectorSearchSpecValues
    """

    _validation = {
        "parameter": {"required": True},
        "operator": {"required": True},
        "values": {"required": True},
    }

    _attribute_map = {
        "parameter": {"key": "parameter", "type": "str"},
        "operator": {"key": "operator", "type": "str"},
        "values": {"key": "values", "type": "VectorSearchSpecValues"},
    }

    def __init__(
        self,
        *,
        parameter: str,
        operator: Union[str, "_models.VectorSearchOperator"],
        values: "_models.VectorSearchSpecValues",
        **kwargs: Any,
    ) -> None:
        """
        :keyword parameter: Parameter. Required.
        :paramtype parameter: str
        :keyword operator: VectorSearchOperator. Required. Known values are: "in" and "not in".
        :paramtype operator: str or ~generated.models.VectorSearchOperator
        :keyword values: Values. Required.
        :paramtype values: ~generated.models.VectorSearchSpecValues
        """
        super().__init__(**kwargs)
        self.parameter = parameter
        self.operator = operator
        self.values = values


class VectorSearchSpecValues(_serialization.Model):
    """Values."""


class VOInfo(_serialization.Model):
    """VOInfo.

    All required parameters must be populated in order to send to server.

    :ivar groups: Groups. Required.
    :vartype groups: dict[str, ~generated.models.GroupInfo]
    :ivar support: SupportInfo. Required.
    :vartype support: ~generated.models.SupportInfo
    :ivar default_group: Default Group. Required.
    :vartype default_group: str
    """

    _validation = {
        "groups": {"required": True},
        "support": {"required": True},
        "default_group": {"required": True},
    }

    _attribute_map = {
        "groups": {"key": "groups", "type": "{GroupInfo}"},
        "support": {"key": "support", "type": "SupportInfo"},
        "default_group": {"key": "default_group", "type": "str"},
    }

    def __init__(
        self,
        *,
        groups: Dict[str, "_models.GroupInfo"],
        support: "_models.SupportInfo",
        default_group: str,
        **kwargs: Any,
    ) -> None:
        """
        :keyword groups: Groups. Required.
        :paramtype groups: dict[str, ~generated.models.GroupInfo]
        :keyword support: SupportInfo. Required.
        :paramtype support: ~generated.models.SupportInfo
        :keyword default_group: Default Group. Required.
        :paramtype default_group: str
        """
        super().__init__(**kwargs)
        self.groups = groups
        self.support = support
        self.default_group = default_group
