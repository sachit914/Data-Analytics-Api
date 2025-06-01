from fastapi import APIRouter
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
    return {"id": 123}

#Put /api/events/
@router.put("/{event_id}")
# def update_event(event_id:int,payload: dict = {}) -> EventSchema:
def update_event(event_id:int,payload: EventUpdateSchema) -> EventSchema:
    print(payload.description)
    return {"id": event_id}

#delete /api/events/
@router.delete("/{event_id}")
def delete_event(event_id:int,payload: dict = {}) -> EventSchema:
    return {"id": event_id}