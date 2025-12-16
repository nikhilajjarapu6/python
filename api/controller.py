from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserRequest, UserResponse
from data import get_db
import service

router = APIRouter(prefix="/api/v1", tags=["Users"])

@router.post("/user", response_model=UserResponse)
def create_user(user: UserRequest, db: Session = Depends(get_db)):
    return service.save_user(db, user)

@router.get("/users", response_model=list[UserResponse])
def fetch_all_users(db: Session = Depends(get_db)):
    return service.get_users(db)

@router.get("/users/{id}",response_model=UserResponse)
def find_user(id:int,db: Session = Depends(get_db)):
    return service.get_user_by_id(db,id)

@router.delete("/users/{id}",response_model=UserResponse)
def delete_user(id:int,db: Session = Depends(get_db)):
    return service.delete_user(db,id)

@router.put("/users/{id}",response_model=UserResponse)
def update_user(id:int,dto:UserRequest,db:Session=Depends(get_db)):
    return service.update_user(db,id,dto)
