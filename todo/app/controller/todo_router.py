from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends,APIRouter
from app.services.todo_service import TodoService
from app.core.database import get_db
from app.schemas.todo import TodoRequest,TodoResponse,TodoUpdate
from app.models.todo import Todo
from typing import List

service=TodoService()
router=APIRouter(prefix="/todos")

@router.post("/save",response_model=TodoResponse)
def create(data:TodoRequest,db:Session=Depends(get_db)):
    return service.create(db,data)

@router.get("/todo_list",response_model=List[TodoResponse])
def find_all(db:Session=Depends(get_db)):
    return service.get_all(db)

@router.get("/get_todo/{id}",response_model=TodoResponse)
def find_By_id(id:int,db:Session=Depends(get_db)):
    return service.find_by_id(db,id)

@router.put("/update/{id}",response_model=TodoResponse)
def update(id:int,data:TodoUpdate,db:Session=Depends(get_db)):
    return service.update(db,id,data)

@router.delete("/delete/{id}",response_model=TodoResponse)
def delete(id:int,db:Session=Depends(get_db)):
    return service.delete(db,id)