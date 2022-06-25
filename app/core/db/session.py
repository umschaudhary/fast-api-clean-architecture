from typing import Generator
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from .base import Base

from app.core.config import get_settings


class Session:
    engine = create_engine(
        get_settings().DATABASE_URL,
        echo=True, pool_pre_ping=True
    )

    @lru_cache
    def create_session(self) -> scoped_session:
        Session = scoped_session(sessionmaker(
            autocommit=False, autoflush=False, bind=engine))
        return Session

    def get_session(self) -> Generator[scoped_session, None, None]:
        db = self.create_session()
        try:
            yield db
        except:
            db.remove()


session = Session()
