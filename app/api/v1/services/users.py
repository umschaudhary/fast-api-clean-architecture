from typing import Union

from sqlalchemy.orm import Session

from app.api.v1.repository import UserRepository
from app.api.v1.schemas import UserCreate
from app.models import User


class UserService:
    """User Service."""

    user_repo = UserRepository()

    def create_user(self, user: UserCreate, db: Session) -> User:
        """
        Create user service.

        returns: User
        """
        return self.user_repo.create_user(user, db)

    def get_user_by_email(self, email: str, db: Session) -> Union[User, bool]:
        """
        Get user by email.

        returns: User or None
        """
        return self.user_repo.get_user_by_email(email, db)

    def authenticate_user(
        self, email: str, password: str, db: Session
    ) -> Union[User, bool]:
        """
        Authenticate user service.

        returns: User or None
        """
        return self.user_repo.authenticate_user(email, password, db)
