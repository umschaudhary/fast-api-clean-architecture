from fastapi import FastAPI, APIRouter, Query, HTTPException
from typing import Optional
from app.core.config import get_settings
from app.api.v1.routes import get_routers
from app.migrations.run import run_sql_migrations


class App:

    settings = get_settings()
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url="/api/v1/openapi.json",
    )

    def start_application(self) -> FastAPI:
        get_routers(self.app)
        return self.app


app = App().start_application()


#  @app.on_event("startup")
#  async def startup_event():
#      run_sql_migrations()
