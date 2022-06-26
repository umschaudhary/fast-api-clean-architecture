from datetime import timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm import Session
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.api.v1.schemas import (ShowUser, UserCreate, UserLogin,
                                UserLoginResponse)
from app.api.v1.services import UserService
from app.core import Hasher, create_access_token, get_settings
from app.core.db import session
from app.models import User

user_router = InferringRouter()


@cbv(user_router)
class UserController:
    """User Controller."""

    user_service = UserService()
    settings = get_settings()
    db: Session = Depends(session.get_session)

    @user_router.post("/", response_model=ShowUser, status_code=HTTP_201_CREATED)
    def create_user(self, user: UserCreate):
        """
        Create a user.

        - **username**: str
        - **email**: str
        - **password**: str
        """
        return self.user_service.create_user(user, self.db)

    @user_router.post(
        "/get-token", response_model=UserLoginResponse, status_code=HTTP_200_OK
    )
    def get_token(self, form_data: UserLogin):
        """
        Get access token for a user.

        - **email**: str
        - **password**: str
        """
        user = self.user_service.authenticate_user(
            form_data.email, form_data.password, self.db
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password!",
            )
        if user and not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User inactive, Please contact administrator!",
            )

        access_token_expires = timedelta(
            minutes=self.settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        access_token = create_access_token(
            data={
                "id": str(user.id),
                "email": user.email,
                "username": user.username,
            },
            expires_delta=access_token_expires,
        )
        response = UserLoginResponse(
            access_token=access_token,
            token_type="Jwt",
            email=user.email,
            username=user.username,
        )

        return response
