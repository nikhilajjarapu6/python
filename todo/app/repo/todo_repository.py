from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoRequest,TodoUpdate

class TodoRepository:
    def create(self,db:Session,data:TodoRequest):
        todo_dict=data.model_dump()
        todo=Todo(**todo_dict)
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo
    def get_all(self,db:Session):
        return db.query(Todo).all()
    def find_user_by_id(self,db:Session,id:int):
       return db.query(Todo).filter(Todo.id==id).first()
    def update(self,db:Session,id:int,data:TodoUpdate):
        todo=db.query(Todo).filter(Todo.id==id).first()
        if not todo:
            return None
        todo_dict=data.model_dump(exclude_unset=True)
        for k,v in todo_dict.items():
            setattr(todo,k,v)
        db.commit()
        db.refresh(todo)

        return todo
    def delete(self,db:Session,id:int):
      todo = db.query(Todo).filter(Todo.id == id).first()
      if todo:
           db.delete(todo)
           db.commit()
      return todo

