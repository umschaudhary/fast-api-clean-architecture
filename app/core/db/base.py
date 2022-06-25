from typing import Any
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )
    __name__: str

    # generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
