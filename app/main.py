from fastapi import FastAPI, APIRouter, Query, HTTPException
from typing import Optional
from app.core.config import get_settings
from app.models import User, Job
from app.api.controllers import page_router


def include_router(app):

    app.include_router(
        page_router,
        prefix="/pages",
        tags=["Pages"],
        responses={404: {"description": "Not found"}}
    )


def start_application():
    settings = get_settings()

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url="/openapi.json"
    )

    include_router(app)
    return app


app = start_application()


@app.on_event("startup")
def on_startup():
    print("------server started------")
