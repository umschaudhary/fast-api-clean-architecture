from fastapi import FastAPI, APIRouter
from app.api.v1.controllers import user_router
from app.core import include_router


def get_routers(app):
    """
    register all routers
    """

    router = [
        include_router(app, user_router, "users", "Users"),
    ]

    return router
