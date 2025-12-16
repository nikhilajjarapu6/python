from passlib.context import CryptContext
from schemas import PersonCreate,TokenData,TokenPayload
from sqlalchemy.orm import Session
from config import ALGORITHAM,SECRET_KEY,ACCESS_TOKEN_EXPIRE_MINUTES
from jose import jwt,JWTError
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from database import get_db


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_context=OAuth2PasswordBearer(tokenUrl="/users/login")


def verify_password(passsword,hashed):
    return pwd_context.verify(passsword,hashed)

def hash_password(password:str):
    return pwd_context.hash(password)

def create_token(data:TokenData):
    cred=data.model_dump()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    cred.update({
        "exp":expire,
        "iat":datetime.utcnow()
    })
    return jwt.encode(cred,SECRET_KEY,algorithm=ALGORITHAM)
def verify_token(token:str=Depends(oauth_context)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHAM])
        return payload
    except JWTError:
        return None
    
def get_current_user(
    token: str = Depends(oauth_context),
    db: Session = Depends(get_db)
):
    from service import PersonService
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHAM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    email = payload.get("sub")
    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    
    # Get user from database
    service = PersonService()
    user = service.get_by_email(db, email)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user