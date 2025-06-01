from fastapi import FastAPI
# from api.events.routing import router as event_router
from api.events import router as event_router


app = FastAPI()
app.include_router(event_router, prefix="/api/events")




@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}