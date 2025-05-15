from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2
router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=schemas.Token)  #response_model is used to define the response schema
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):  #user_credentials: schemas.UserLogin
    #username = user_credentials.username
    {
        'username': "dss",
        'password': "jdjdkw"

    }
#oAuth2PasswordRequestForm is a class that is used to get the username and password from the user
#we can use it to test the postman not the raw but form-data

    #password = user_credentials.password
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password): #verify the password
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    #create a token
    #return token
    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"} #returning the token
#addition to pass the login to main.py file