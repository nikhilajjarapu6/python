from pydantic import BaseModel

class UserRequest(BaseModel): #input dto
    name:str
    email:str

class UserResponse(BaseModel): #output dto
    id:int
    name:str
    email:str

    model_config = {"from_attributes": True}