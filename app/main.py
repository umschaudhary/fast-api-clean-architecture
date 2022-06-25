from fastapi import FastAPI, APIRouter, Query, HTTPException
from typing import Optional
from app.core.config import get_settings
from app.models import User, Job
from app.api.v1.routes import api_router


class App:

    settings = get_settings()
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url="/api/v1/openapi.json"
    )

    def start_application(self):
        self.app.include_router(api_router)
        return self.app


app = App().start_application()
