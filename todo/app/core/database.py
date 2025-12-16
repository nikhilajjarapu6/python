from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine

DATABASE_URL="mysql+pymysql://root:root@localhost:3306/python"
engine=create_engine(DATABASE_URL,echo=True)
SessionLocal=sessionmaker(autocommit=False,bind=engine,autoflush=False)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()