from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.schemas.todo import TodoResponse

class UserRequest(BaseModel):
    username:str|None
    full_name:str|None
    email:str|None
    password:str|None

class UserUpdate(BaseModel):
    username: str | None = None
    full_name: str | None = None
    email: str | None = None
    password: str | None = None

class UserResponse(BaseModel):
    id:int
    username:str|None
    full_name:str|None
    email:str|None
    password:str|None
    created_at:datetime|None
    updated_at:datetime|None
    todos:List[TodoResponse]=[]

    model_config={"from_attributes":True} 