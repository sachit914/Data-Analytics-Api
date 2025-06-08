import sqlmodel
from sqlmodel import SQLModel,Session
from .config import DATABSE_URL

if DATABSE_URL=="":
    raise NotImplementedError("Database URL is not set. Please set the DATABSE_URL environment variable.")

engine = sqlmodel.create_engine(DATABSE_URL)


def init_db():
    print("creating database")
    SQLModel.metadata.create_all(engine)

    
def get_session():
    with Session(engine) as session:
        yield session