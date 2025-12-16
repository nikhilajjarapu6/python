from sqlalchemy.orm import Session
from app.repo.user_repo import UserRepo
from app.schemas.user import UserRequest,UserUpdate
from fastapi import HTTPException

class UserService:
    def __init__(self):
        self.repo=UserRepo()
    def create(self,db:Session,data:UserRequest):
        return self.repo.create(db,data)
    def find_all(self,db:Session):
        return self.repo.find_all(db)
    def find_by_id(self,db:Session,id:int):
        user=self.repo.find_by_id(db,id)
        if not user:
            raise HTTPException(status_code=404,detail=f"User not found with id:{id}")
        return user
    def update(self,db:Session,id:int,data:UserUpdate):
        user=self.repo.update(db,id,data)
        if not user:
            raise HTTPException(status_code=404,detail=f"User not found with id:{id}")
        return user
    def delete(self,db:Session,id:int):
        user=self.repo.delete(db,id)
        if not user:
            raise HTTPException(status_code=404,detail=f"User not found with id:{id}")
        return user
