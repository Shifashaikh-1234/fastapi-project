from sqlalchemy import Column, Integer, String,Boolean, ForeignKey
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class Post(Base): # SQLAlchemy model what each table will look like - for defining the columns of our posts table
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete ="CASCADE"),nullable= False )
     # foreign key to the users table

    owner = relationship("User") #relationship to the users table - to get the user who created the post

Post_Pydantic = Post #addition to pass the PostResponse to main.py file



class User(Base): # SQLAlchemy model what each table will look like - for defining the columns of our users table
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

Post_Pydantic = User #addition to pass the UserResponse to main.py file


class Vote(Base): # SQLAlchemy model what each table will look like - for defining the columns of our votes table
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id", ondelete ="CASCADE"), primary_key=True, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete ="CASCADE"), primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)