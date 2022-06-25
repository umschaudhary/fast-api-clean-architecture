from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db import session
from app.models import User
from app.core.hashing import Hasher

from app.api.v1.schemas import UserCreate


class UserRepository:

    def create_user(self, user: UserCreate, db: Session):
        user = User(
            username=user.username,
            email=user.email,
            password=Hasher.get_hashed_password(user.password),
            is_active=True,
            is_superuser=False
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
