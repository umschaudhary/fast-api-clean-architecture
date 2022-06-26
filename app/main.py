from fastapi import APIRouter, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import get_routers
from app.core.config import get_settings
from app.migrations.run import run_sql_migrations


class App:

    """Entry Point."""

    settings = get_settings()
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        openapi_url="/api/v1/openapi.json",
    )

    def add_cors(self):
        """Add cors method."""

        origins = [
            "http://localhost",
            "http://localhost:8080",
        ]
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def start_application(self) -> FastAPI:
        """Start application method."""

        get_routers(self.app)
        self.add_cors()
        return self.app


app = App().start_application()


#  @app.on_event("startup")
#  async def startup_event():
#      run_sql_migrations()
