from datetime import datetime
from typing import Any, Dict

from sqlalchemy import Boolean, Column, DateTime, func, inspect
from sqlalchemy.orm import as_declarative, declared_attr  # type: ignore
from sqlalchemy_mixins import AllFeaturesMixin


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __asdict__(self) -> Dict:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class BaseModel(Base, AllFeaturesMixin):
    __abstract__ = True
    deleted = Column(Boolean(), default=False)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at: datetime = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )

    __mapper_args__ = {"eager_defaults": True}
