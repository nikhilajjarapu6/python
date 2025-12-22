from fastapi import FastAPI,HTTPException,APIRouter,Depends
from app.services.user_service import UserService
from app.schemas.user import UserResponse,UserCreate,UserUpdate
from app.database.database import get_db
from app.models.user import User
from sqlalchemy.orm import Session

user_router=APIRouter(prefix="/users")

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


@user_router.post("/save",response_model=UserResponse)
def create(user:UserCreate,service:UserService=Depends(get_user_service),db:Session=Depends(get_db)):
    return service.create_user(user)

@user_router.get("/find_by_id/{id}",response_model=UserResponse)
def find_by_id(id:int,service:UserService=Depends(get_user_service),db:Session=Depends(get_db)):
    return service.get_user_by_id(id)

@user_router.post("/find_by_email",response_model=UserResponse)
def find_by_email(email:str,service:UserService=Depends(get_user_service),db:Session=Depends(get_db)):
    return service.get_user_by_email(email)

@user_router.post("/find_by_mobile",response_model=UserResponse)
def find_by_mobile(mobile:int,service:UserService=Depends(get_user_service),db:Session=Depends(get_db)):
    return service.find_by_mobile(mobile)

@user_router.put("/update/{id}")
def update(id:int,user:UserCreate,service:UserService=Depends(get_user_service),db:Session=Depends(get_db)):
    return service.update_user(id,user)