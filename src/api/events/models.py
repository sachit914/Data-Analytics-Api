# from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field


class EventSchema(SQLModel):
    id: int
    page:Optional[str] = ""
    description: Optional[str] = ""


class EvenetCreateSchema(SQLModel):
    page:str
    description: Optional[str] = ""

class EventUpdateSchema(SQLModel):
    description: str 

# returns list of eventSchema and count
class EventListSchema(SQLModel):
    results: list[EventSchema]
    count: int
