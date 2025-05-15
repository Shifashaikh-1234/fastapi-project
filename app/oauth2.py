from jose import jwt, JWTError

from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #to get the token from the request



#SECRET_KEY
#ALGORITHM
#ACCESS_TOKEN_EXPIRE_MINUTES

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    
    
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

create_access_token({"sub": "test"})

def verify_access_token(token: str, credentials_exception):
    try:
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        id: str = payload.get("user_id")


        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    #except JWTError:
    
    return token_data #id id returned from the token
    #return token_data

#to get the current user from the token


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db) ):   #take the token from the request and extract id for us and verif
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=f"Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token, credentials_exception) #verify the token and return the user id
    user = db.query(models.User).filter(models.User.id == token.id).first() #get the user from the database
    return 

get_current_user(token="token")

