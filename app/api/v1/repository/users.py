from typing import Union

from sqlalchemy.orm import Session

from app.api.v1.schemas import UserCreate
from app.core.db import session
from app.core.hashing import Hasher
from app.models import User


class UserRepository:
    """User Repository."""

    def create_user(self, user: UserCreate, db: Session) -> User:
        """
        Create user repository.

        returns: User
        """
        new_user = User(
            username=user.username,
            email=user.email,
            password=Hasher.get_hashed_password(user.password),
            is_active=True,
            is_superuser=False,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_user_by_email(self, email: str, db: Session) -> Union[User, bool]:
        """
        Get user by email.

        returns: User or None
        """
        user = db.query(User).filter(User.email == email).first()
        return user

    def authenticate_user(
        self, email: str, password: str, db: Session
    ) -> Union[User, bool]:
        """
        Authenticate user repository.

        returns: User or None
        """
        user = self.get_user_by_email(email, db)

        if not user:
            return False

        if not Hasher.verify_password(password, user.password):
            return False
        return user
