from fastapi import APIRouter
import os

from api.db.config import DATABSE_URL

from .schemas import(
     EventSchema,
     EventListSchema,
     EvenetCreateSchema,
     EventUpdateSchema
)


router = APIRouter()

#GET /api/events/
@router.get("/")
# return data type is EventListSchema
def read_events() -> EventListSchema:
    # returns list of items
    print(os.environ.get('DATABASE_URL'),"ssssssssss",DATABSE_URL)
    return {
        "results": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ],
        "count": 3
    }

#GET /api/events/{event_id}
@router.get("/{event_id}")
# int is incoming data type ,eventSchema is outgoing data type
def read_event(event_id:int) -> EventSchema:
    # returns single item
    return {"id": event_id}


#POST /api/events/
@router.post("/")
# def create_event(payload:dict = {}) -> EventSchema:
def create_event(payload: EvenetCreateSchema) -> EventSchema:
    print(payload)
    data = payload.model_dump()  #payload ->dict ->pydantic
    return {"id": 123,**data}

#Put /api/events/
@router.put("/{event_id}")
# def update_event(event_id:int,payload: dict = {}) -> EventSchema:
def update_event(event_id:int,payload: EventUpdateSchema) -> EventSchema:
    print(payload.description)
    data = payload.model_dump()

    return {"id": event_id,**data}

#delete /api/events/
@router.delete("/{event_id}")
def delete_event(event_id:int,payload: dict = {}) -> EventSchema:
    return {"id": event_id}