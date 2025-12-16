from pydantic import BaseModel

class LoginRequest(BaseModel):
    email:str
    password:str

class LoginResponse(BaseModel):
    message:str
    username:str
    userid:int

    model_config={
        "from_attributes":True
    }