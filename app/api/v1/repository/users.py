from sqlalchemy.orm import Session
from app.core.db import session
from app.models import User
from app.core.hashing import Hasher

from app.api.v1.schemas import UserCreate


class UserRepository:
    def create_user(self, user: UserCreate, db: Session) -> User:
        user = User(
            username=user.username,
            email=user.email,
            password=Hasher.get_hashed_password(user.password),
            is_active=True,
            is_superuser=False,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_email(self, email: str, db: Session) -> User:
        user = db.query(User).filter(User.email == email).first()
        return user

    def authenticate_user(self, email: str, password: str, db: Session) -> User:
        user = self.get_user_by_email(email, db)

        if not user:
            return False

        if not Hasher.verify_password(password, user.password):
            return False
        return user
