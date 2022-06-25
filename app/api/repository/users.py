from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.db import session

from app.api.schemas import UserCreate


class UserRepository:
    db: Session = session.get_session()

    def create_user(self, user: UserCreate):
        pass
