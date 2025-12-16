from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime

class Todo(Base):
    __tablename__ = "todos"   # table names should be lowercase

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)      
    schedule_time = Column(DateTime, nullable=False)
    status = Column(String(255), nullable=True)   
    user_id=Column(Integer,ForeignKey("users.id"))
    user=relationship("User",back_populates="todos")   
