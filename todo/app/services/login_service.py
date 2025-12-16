from sqlalchemy.orm import Session
from app.repo.login_repo import LoginRepo
from app.schemas.login import LoginRequest,LoginResponse
from fastapi import HTTPException

class LoginService:
    def __init__(self):
        self.repo=LoginRepo()
    def login(self,db:Session,login_obj:LoginRequest):
        user=self.repo.login(db,login_obj)

        if not user:
            raise HTTPException(status_code=404,detail=f"check you email and password")
        
        return LoginResponse (
            message="Login successfull",
            username=user.username,
            userid=user.id
            )
