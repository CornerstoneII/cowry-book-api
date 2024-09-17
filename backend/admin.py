from fastapi import FastAPI
from backend.routes import router as admin_router
from db import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin_router)
