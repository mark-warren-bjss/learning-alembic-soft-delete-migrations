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

    @classmethod
    def uniqueish(cls, *fields):
        table_name = cls.__name__.lower()
        field_names = '_'.join(f.name for f in fields)
        cls.__table_args__ = getattr(cls, '__table_args__', ()) + (
            Index(f"idx_{table_name}_{field_names}_notdeleted", *fields, 'deleted_at',
                  unique=True,
                  postgresql_where='deleted_at IS NULL'),
            Index(f"idx_{table_name}_{field_names}_deleted", *fields,
                  unique=True,
                  postgresql_where='deleted_at IS NOT NULL'),
        )
