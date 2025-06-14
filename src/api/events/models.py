# from pydantic import BaseModel
from typing import Optional
import sqlmodel
from sqlmodel import SQLModel, Field
from datetime import datetime,timezone


def get_utc_now():
    return datetime.now(timezone.utc).replace(tzinfo=timezone.utc)


class EventModel(SQLModel,table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    page:Optional[str] = ""
    description: Optional[str] = ""
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlmodel.DateTime(timezone=True),
        nullable=False
    )


class EvenetCreateSchema(SQLModel):
    page:str
    description: Optional[str] = ""

class EventUpdateSchema(SQLModel):
    description: str 

# returns list of eventSchema and count
class EventListSchema(SQLModel):
    results: list[EventModel]
    count: int
