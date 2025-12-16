from fastapi import APIRouter,Depends,HTTPException
from service import PersonService
from database import get_db
from sqlalchemy.orm import Session
from schemas import PersonCreate,PersonResponse,TokenData,TokenPayload,Login,TokenResponse
from typing import List
from auth import hash_password,verify_password,create_token,get_current_user as current_user
from model import Person

service=PersonService()
router=APIRouter(prefix="/users")

@router.post("/signup", response_model=PersonResponse)
def signup(user: PersonCreate, db: Session = Depends(get_db)):
    return service.create(db, user)


@router.post("/login", response_model=TokenResponse)
def login(data: Login, db: Session = Depends(get_db)):
    user = service.authenticate(db, data.email, data.password)
    token = create_token(TokenData(sub=user.email))
    return {"access_token": token, "token_type": "bearer"}

@router.get("/find/{id}",response_model=PersonResponse)
def get_person(id:int,current:Person=Depends(current_user),db:Session=Depends(get_db)):
        user=service.get_person(db,id)
        return user
@router.get("/all",response_model=List[PersonResponse])
def get_all(curent:Person=Depends(current_user), db:Session=Depends(get_db)):
        return service.get_all(db)

@router.put("/update/{id}",response_model=PersonResponse)
def update(id:int,person:PersonCreate,current:Person=Depends(current_user),db:Session=Depends(get_db)):
        return service.update(db,id,person)

@router.delete("/delete/{id}",response_model=PersonResponse)
def delete(id:int,current:Person=Depends(current_user),db:Session=Depends(get_db)):
        return service.delete(db,id)
