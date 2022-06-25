from fastapi import FastAPI, APIRouter
from app.api.v1.controllers import user_router
from app.core import include_router

api_router = APIRouter()

include_router(api_router, user_router, "users", "Users")
