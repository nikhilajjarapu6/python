from fastapi import FastAPI
from app.core.database import Base,engine
from app.controller.todo_router import router
from app.controller.user_router import user_router
from app.models import user,todo

Base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(router)
app.include_router(user_router)