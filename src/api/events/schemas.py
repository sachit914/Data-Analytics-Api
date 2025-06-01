from pydantic import BaseModel

class EvenetCreateSchema(BaseModel):
    page:str

class EventUpdateSchema(BaseModel):
    description: str 

class EventSchema(BaseModel):
    id: int

# returns list of eventSchema and count
class EventListSchema(BaseModel):
    results: list[EventSchema]
    count: int
