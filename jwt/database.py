from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

URL="mysql+pymysql://root:root@localhost:3306/python"
engine=create_engine(URL,echo=True)
SessionLocal=sessionmaker(autocommit=False,bind=engine,autoflush=True)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()