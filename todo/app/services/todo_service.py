from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repo.todo_repository import TodoRepository
from app.schemas.todo import TodoRequest,TodoUpdate

class TodoService:
    def __init__(self):
        self.repo=TodoRepository()
    def create(self,db:Session,data:TodoRequest):
        return self.repo.create(db,data)
    def get_all(self,db:Session):
        return self.repo.get_all(db)
    def find_by_id(self,db:Session,id:int):
        todo=self.repo.find_user_by_id(db,id)
        if not todo:
            raise HTTPException(status_code=404,detail=f"Todo not found with id {id}")
        return todo
    def update(self,db:Session,id:int,data:TodoUpdate):
        updated_todo = self.repo.update(db, id, data)
        if not updated_todo:
            raise HTTPException(status_code=404, detail=f"Todo not found with id {id}")
        return updated_todo
    def delete(self,db:Session,id:int):
        deleted_todo = self.repo.delete(db, id)
        if not deleted_todo:
            raise HTTPException(status_code=404, detail=f"Todo not found with id {id}")
        return deleted_todo
        