
from fastapi import APIRouter,Depends,HTTPException
from api.db.session import get_session
from sqlmodel import Session,select
import os

from api.db.config import DATABSE_URL

from .models import(
     EventModel,
     EventListSchema,
     EvenetCreateSchema,
     EventUpdateSchema
)


router = APIRouter()

#GET /api/events/
@router.get("/",response_model=EventListSchema)
# return data type is EventListSchema
def read_events(session:Session = Depends(get_session)):
    query = select(EventModel).order_by(EventModel.id.desc()).limit(10)
    results = session.exec(query).all() 
    return {
        "results":  results,
        "count": len(results)
    }

#GET /api/events/{event_id}
@router.get("/{event_id}",response_model=EventModel)
# int is incoming data type ,eventSchema is outgoing data type
def get_event(event_id:int,session:Session= Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    result = session.exec(query).first() 
    if not result:
        raise HTTPException(status_code = 404,detail = "Event not found")
    return result


#POST /api/events/
@router.post("/",response_model=EventModel)
def create_event(
    payload: EvenetCreateSchema,
    session:Session = Depends(get_session)):
    
    print(payload)
    data = payload.model_dump() #payload ->dict ->pydantic
    obj = EventModel.model_validate(data) #pydantic ->sqlmodel
    session.add(obj)
    session.commit()
    session.refresh(obj) #refresh the object to get the id and other fields populated
    return obj

#Put /api/events/
@router.put("/{event_id}",response_model=EventModel)
def update_event(
    event_id:int,
    payload: EventUpdateSchema,
    Session:Session = Depends(get_session)):

    query = select(EventModel).where(EventModel.id == event_id)
    obj = Session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Event not found")  
    data = payload.model_dump()
    for key, value in data.items():
        setattr(obj, key, value)
    Session.add(obj)
    Session.commit()
    Session.refresh(obj)

    return obj

#delete /api/events/
@router.delete("/{event_id}")
def delete_event(event_id:int,payload: dict = {}) -> EventModel:
    return {"id": event_id}