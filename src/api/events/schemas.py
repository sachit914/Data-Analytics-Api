from pydantic import BaseModel
from typing import Optional

class EvenetCreateSchema(BaseModel):
    page:str
    description: Optional[str] = ""

class EventUpdateSchema(BaseModel):
    description: str 

class EventSchema(BaseModel):
    id: int
    page:Optional[str] = ""
    description: Optional[str] = ""

# returns list of eventSchema and count
class EventListSchema(BaseModel):
    # results: list[EventSchema]
    count: int
