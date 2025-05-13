
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Post(BaseModel): #pydantic model - it defines the structure of request and response body - schema - validation to body
    title: str
    content: str
    published: bool = True

Post_Pydantic = Post

#class CreatePost(BaseModel):
    #title: str
    #content: str
    #published: bool = True

#class UpdatePost(BaseModel):
    #published: bool  #we allow user to update only published field

#instead of creating two classes we can use the same class for both create and update

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
    #title: str
    #content: str
    #published: bool
    id: int
    created_at: datetime
    #created_at: datetime = Field(default_factory=datetime.utcnow) #to set the default value of created_at to current time
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


class UserOut(BaseModel): #response model - it defines the structure of response body - schema - validation to body
    id: int
    email: EmailStr
    created_at: datetime
    

    class Config:
        orm_mode = True  #to tell pydantic to convert the data from SQLAlchemy model to pydantic model

Post_Pydantic = UserOut  #addition to pass the UserOut to main.py file


class UserLogin(BaseModel): #pydantic model - it defines the structure of request and response body - schema - validation to body
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


Post_Pydantic = UserLogin  #addition to pass the UserLogin to main.py file