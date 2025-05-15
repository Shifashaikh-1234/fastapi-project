
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

class UserOut(BaseModel): #response model - it defines the structure of response body - schema - validation to body
    id: int
    email: EmailStr
    created_at: datetime
    

    class Config:
        orm_mode = True  #to tell pydantic to convert the data from SQLAlchemy model to pydantic model

Post_Pydantic = UserOut

class Post(BaseModel): #pydantic model - it defines the structure of request and response body - schema - validation to body
    title: str
    content: str
    published: bool = True
    owner: UserOut

Post_Pydantic = Post

#class CreatePost(BaseModel):
    #title: str
    #content: str
    #published: bool = True

#class UpdatePost(BaseModel):
    #published: bool  #we allow user to update only published field
#instead of creating two classes we can use the same class for both create and update


class PostOut(BaseModel): #response model - it defines the structure of response body - schema - validation to body
    Post: Post
    votes: int 

    class Config:
        orm_mode = True
    
     #to get the number of votes for the post

Post_Pydantic = PostOut  #addition to pass the PostOut to main.py file
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase): #inherits from PostBase
    pass

Post_Pydantic = PostCreate  #addition to pass the PostCreate to main.py file

#class UpdatePost(PostBase): #inherits from PostBase
    #pass


#-------------------------------------------------------------------------------------#



class Post(PostBase):  #response model - it defines the structure of response body - schema - validation to body
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut #to get the user details who created the post
    class Config:
        orm_mode = True  #to tell pydantic to convert the data from SQLAlchemy model to pydantic model
    #orm_mode = True is used to tell pydantic to use the ORM mode, which allows us to use SQLAlchemy models directly with pydantic models.
    #This is useful when we want to return SQLAlchemy models as response models in FastAPI.

Post_Pydantic = Post #addition to pass the PostResponse to main.py file

#-------------------------------------------------------------------------------------#
class UserCreate(BaseModel): #pydantic model - it defines the structure of request and response body - schema - validation to body
    email: EmailStr
    password: str

Post_Pydantic = UserCreate  #addition to pass the UserCreate to main.py file

  #addition to pass the UserOut to main.py file


class UserLogin(BaseModel): #pydantic model - it defines the structure of request and response body - schema - validation to body
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


Post_Pydantic = UserLogin  #addition to pass the UserLogin to main.py file

#Schemas for the token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):  #for the data to be embedded in the token
    id: Optional[str] = None
    
    #user_id: int
    #email: EmailStr
    #password: str
    #created_at: datetime
    #class Config:
        #orm_mode = True  #to tell pydantic to convert the data from SQLAlchemy model to pydantic model


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)  #conint is used to validate the integer value to be between 0 and 1
    #user_id: int
    #class Config:
        #orm_mode = True  #to tell pydantic to convert the data from SQLAlchemy model to pydantic model