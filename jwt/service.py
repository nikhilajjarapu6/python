from sqlalchemy.orm import Session
from schemas import PersonCreate
from model import Person
from auth import hash_password,verify_password,create_token
from exceptions import (
    PersonNotFound,
    PersonAlreadyExists,
    InvalidCredentials
)


class PersonService:
    def __init__(self):
        pass

    def create(self,db:Session,data:PersonCreate):
        if self.get_by_email(db, data.email):
            raise PersonAlreadyExists(
                f"Person with email '{data.email}' already exists"
            )
        hashed=hash_password(data.password)
        person=Person(
            name=data.name,
            email=data.email,
            password=hashed
        )
        db.add(person)
        db.commit()
        db.refresh(person)

        return person

    def get_by_email(self,db:Session,email:str):
        person=db.query(Person).filter(Person.email==email).first()
        if not person:
            raise PersonNotFound(f"Person with email {email} not found")
        return person
    def get_by_name(self,db:Session,name:str):
        person=db.query(Person).filter(Person.name==name).first()
        if not person:
            raise PersonNotFound(f"Person with name {name} not found")
        return person
    def get_person(self,db:Session,id:int):
        person=db.query(Person).filter(Person.id==id).first()
        if not person:
            raise PersonNotFound(f"Person with id {id} not found")
        return person
    
    def get_all(self,db:Session):
        return db.query(Person).all()

    def authenticate(self,db:Session,email:str,password:str):
        db_user=self.get_by_email(db,email)
        if not db_user:
            raise InvalidCredentials()
        
        if not verify_password(password,db_user.password):
            raise InvalidCredentials()
        return db_user
    
    def update(self,db:Session,id:int,person:PersonCreate):
        db_person=db.query(Person).filter(Person.id==id).first()
        if not db_person :
            raise PersonNotFound(f"Person with id {id} not found")
        person_dict=person.model_dump(exclude_unset=True)
        for k,v in person_dict.items():
            setattr(db_person,k,v)
        db.commit()
        db.refresh(db_person)
        return db_person
    def delete(self,db:Session,int:id):
        person=db.query(Person).filter(Person.id==id).first()
        if not person:
            raise PersonNotFound(f"Person with id {id} not found")
        db.delete(person)
        return person
            
