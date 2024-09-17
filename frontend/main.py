from fastapi import FastAPI
from frontend.routes import router as frontend_router
from db import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(frontend_router)
