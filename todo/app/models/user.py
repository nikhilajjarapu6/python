from sqlalchemy import Column,Integer,String,DateTime
from app.core.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime
class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(255),unique=True,nullable=False)
    full_name=Column(String(255),nullable=False)
    email=Column(String(255),unique=True,nullable=False)
    password=Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    todos=relationship("Todo", back_populates="user")