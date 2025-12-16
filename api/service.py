from sqlalchemy.orm import Session
import repo

def save_user(db: Session, dto):
    return repo.user_save(db, dto)

def get_users(db: Session):
    return repo.get_users(db)

def get_user_by_id(db:Session,user_id):
    return repo.get_user_by_id(db,user_id)

def delete_user(db:Session,id):
    return repo.delete_user(db,id)
def update_user(db:Session,id,dto):
    return repo.update_user(db,id,dto)
