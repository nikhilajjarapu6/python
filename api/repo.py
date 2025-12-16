from sqlalchemy.orm import Session
from models import User
from schemas import UserRequest

def user_save(db: Session, user: UserRequest):
    new_user = User(**user)  # DTO → Entity
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(User).all()  

def get_user_by_id(db:Session,user_id:int):
    return db.query(User).filter(User.id==user_id).first()

def delete_user(db:Session,user_id:int):
    user=db.query(User).filter(User.id==user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
def update_user(db:Session,id:int,update_user:UserRequest):
    user=db.query(User).filter(User.id==id).first()

    if not user:
        return None
    updated=update_user.dict(exclude_unset=True)
    for k,v in updated.items():
        setattr(user,k,v)
    
    db.commit()
    db.refresh(user)
    return user