import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import BaseModel


class Appeal(BaseModel):
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    excuse = Column(String, nullable=True)
    name = Column(String, nullable=False, unique=True)


Appeal.uniqueish(Appeal.name)
