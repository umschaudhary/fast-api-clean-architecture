from fastapi import Depends
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

from app.core.db import session
from app.api.v1.schemas import UserCreate, ShowUser
from app.api.v1.services import UserService

user_router = InferringRouter()


@cbv(user_router)
class UserController:
    user_service = UserService()

    @user_router.post("/", response_model=ShowUser, status_code=HTTP_201_CREATED)
    def create_user(self, user: UserCreate, db: Session = Depends(session.get_session)):
        return self.user_service.create_user(user, db)
