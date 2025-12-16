from sqlalchemy.orm import Session
from app.schemas.login import LoginRequest
from app.models.user import User

class LoginRepo:
    def login(self,db:Session,login_obj:LoginRequest):
       return db.query(User).filter(User.email==login_obj.email,User.password==login_obj.password).first()
