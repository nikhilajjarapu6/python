from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserRequest,UserResponse,UserUpdate

class UserRepo:
    def create(self,db:Session,data:UserRequest):
        data_dict=data.model_dump()
        user=User(**data_dict)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    def find_all(self,db:Session):
        return db.query(User).all()
    
    def find_by_id(self,db:Session,id:int):
        return db.query(User).filter(User.id==id).first()
    
    def update(self,db:Session,id:int,data:UserUpdate):
        user=db.query(User).filter(User.id==id).first()
        if not user:
            return None
        update_user=data.model_dump(exclude_unset=True)
        for k,v in update_user.items():
            setattr(user,k,v)
        db.commit()
        db.refresh(user)
        return user
    def delete(self,db:Session,id:int):
        user=db.query(User).filter(User.id==id).first()
        if user:
            db.delete(user)
            db.commit()
        return user
