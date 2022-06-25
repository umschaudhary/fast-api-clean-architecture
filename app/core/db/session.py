from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker

from app.core.config import get_settings

from .base import Base


class DBSession:
    """DB Session."""

    engine = create_engine(get_settings().DATABASE_URL, echo=True, pool_pre_ping=True)

    @lru_cache
    def create_session(self) -> scoped_session:
        """DB Session Creation."""
        Session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        return Session

    def get_session(self) -> Generator[scoped_session, None, None]:
        """Get DB Session."""
        db = self.create_session()
        try:
            yield db
        except:
            db.remove()


session = DBSession()
