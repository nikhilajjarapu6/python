from pydantic import BaseModel

class PersonCreate(BaseModel):
    name: str
    email: str
    password: str

class PersonResponse(BaseModel):
    id: int
    name: str
    email: str

    model_config = {
        "from_attributes": True
    }

class TokenData(BaseModel):
    sub:str

class TokenPayload(BaseModel):
    sub:str
    exp:int
    iat:int

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class Login(BaseModel):
    email:str
    password:str

