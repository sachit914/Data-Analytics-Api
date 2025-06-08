from contextlib import asynccontextmanager
from fastapi import FastAPI
# from api.events.routing import router as event_router
from api.events import router as event_router
from api.db.session import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup
    init_db()
    yield
    #cleanup after app shutdown

app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix="/api/events")

# @app.on_event("startup")
# def on_startup():
#     init_db()           old way of initializing db

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}