# from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field


class EventModel(SQLModel,table=True):
    id:Optional[int] = Field(default=None, primary_key=True)
    page:Optional[str] = ""
    description: Optional[str] = ""


class EvenetCreateSchema(SQLModel):
    page:str
    description: Optional[str] = ""

class EventUpdateSchema(SQLModel):
    description: str 

# returns list of eventSchema and count
class EventListSchema(SQLModel):
    results: list[EventModel]
    count: int
