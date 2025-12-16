from pydantic import BaseModel
from datetime import datetime
class TodoRequest(BaseModel):
    title:str
    description:str|None
    schedule_time:datetime
    status:str|None

class TodoUpdate(BaseModel):
    title:str
    description:str|None
    schedule_time:datetime
    status:str|None

class TodoResponse(BaseModel):
    id:int
    title:str
    description:str|None
    schedule_time:datetime
    status:str|None
    user_id:int

    model_config = {
        "from_attributes": True
    }