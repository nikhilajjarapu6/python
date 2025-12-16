import controller
from data import Base, engine
from fastapi import FastAPI

app=FastAPI()
# Create DB tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(controller.router)
