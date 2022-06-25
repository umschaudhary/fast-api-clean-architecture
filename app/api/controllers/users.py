from fastapi import Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session

from app.api.schemas import UserCreate
from app.core.db import session
from app.api.services import UserService

user_router = InferringRouter()


@cbv(user_router)
class UserController:
    user_service = UserService()

    @user_router.post("/")
    def create_user(self, user: UserCreate):
        return self.user_service.user_service.create_user(user)
