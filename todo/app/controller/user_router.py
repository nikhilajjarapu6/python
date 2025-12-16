from fastapi import FastAPI,Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.user_service import UserService
from app.schemas.user import UserResponse,UserRequest,UserUpdate
from typing import List
from app.schemas.login import LoginResponse,LoginRequest
from app.services.login_service import LoginService

service=UserService()
loginservice=LoginService()
user_router=APIRouter(prefix="/users")

@user_router.post("/save",response_model=UserResponse)
def create(user:UserRequest,db:Session=Depends(get_db)):
    return service.create(db,user)

@user_router.get("/list",response_model=List[UserResponse])
def find_all(db:Session=Depends(get_db)):
    return service.find_all(db)

@user_router.get("/find/{id}")
def find_buy_id(id:int,db:Session=Depends(get_db)):
    return service.find_by_id(db,id)

@user_router.put("/update/{id}",response_model=UserResponse)
def update(id:int,user:UserUpdate,db:Session=Depends(get_db)):
    return service.update(db,id,user)

@user_router.delete("/delete/{id}",response_model=UserResponse)
def delete(id:int,db:Session=Depends(get_db)):
    return service.delete(db,id)

@user_router.post("/login",response_model=LoginResponse)
def login(login_obj:LoginRequest,db:Session=Depends(get_db)):
    return loginservice.login(db,login_obj)