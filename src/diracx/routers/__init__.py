from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse, Response
from fastapi.routing import APIRoute

from diracx.core.exceptions import DiracError, DiracHttpResponse
from diracx.db import AuthDB, JobDB

from . import auth, configuration, job_manager

# Rules:
# All routes must have tags (needed for auto gen of client)
# Form headers must have a description (autogen)
# methods name should follow the generate_unique_id_function pattern


def generate_unique_id_function(route: APIRoute) -> str:
    return f"{route.tags[0]}_{route.name}"


class DiracFastAPI(FastAPI):
    def __init__(self):
        super().__init__(
            swagger_ui_init_oauth={
                "clientId": auth.DIRAC_CLIENT_ID,
                "scopes": "group:lhcb_user property:NormalUser",
                "usePkceWithAuthorizationCodeGrant": True,
            },
            generate_unique_id_function=generate_unique_id_function,
            title="Dirac",
        )

    def openapi(self, *args, **kwargs):
        if not app.openapi_schema:
            super().openapi(*args, **kwargs)
            for _, method_item in app.openapi_schema.get("paths").items():
                for _, param in method_item.items():
                    responses = param.get("responses")
                    # remove 422 response, also can remove other status code
                    if "422" in responses:
                        del responses["422"]
        return app.openapi_schema


app = DiracFastAPI()


@app.exception_handler(DiracError)
async def dirac_error_handler(request: Request, exc: DiracError) -> Response:
    return JSONResponse(
        status_code=exc.http_status_code, content={"detail": exc.detail}
    )


@app.exception_handler(DiracHttpResponse)
async def http_response_handler(request: Request, exc: DiracHttpResponse) -> Response:
    return JSONResponse(status_code=exc.status_code, content=exc.data)


app.include_router(
    auth.router,
    prefix="/auth",
)
app.include_router(
    job_manager.router,
    prefix="/jobs",
    dependencies=[Depends(auth.verify_dirac_token)],
)
app.include_router(
    configuration.router,
    prefix="/config",
    dependencies=[Depends(auth.verify_dirac_token)],
)


@app.on_event("startup")
async def startup() -> None:
    await JobDB.make_engine("sqlite+aiosqlite:///:memory:")
    await AuthDB.make_engine("sqlite+aiosqlite:///:memory:")


@app.on_event("shutdown")
async def shutdown() -> None:
    await JobDB.destroy_engine()
    await AuthDB.destroy_engine()


@app.get("/.well-known/openid-configuration", tags=["well-known"])
async def openid_configuration():
    return {
        "issuer": auth.ISSUER,
        "token_endpoint": "http://localhost:8000/auth/lhcb/token",
        "authorization_endpoint": "http://localhost:8000/auth/lhcb/authorize",
        # "introspection_endpoint":"",
        # "userinfo_endpoint":"",
        "grant_types_supported": [
            "authorization_code",
            "urn:ietf:params:oauth:grant-type:device_code",
        ],
        "scopes_supported": [
            "group:lhcb_user",
            "property:NormalUser",
            "property:FileCatalogManagement",
        ],
        "response_types_supported": ["code"],
        "token_endpoint_auth_signing_alg_values_supported": [auth.ALGORITHM],
        "token_endpoint_auth_methods_supported": ["none"],
        "code_challenge_methods_supported": ["S256"],
        "device_authorization_endpoint": "http://localhost:8000/auth/lhcb/device",
    }