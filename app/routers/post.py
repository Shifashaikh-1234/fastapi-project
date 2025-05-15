from .. import models, schemas, utils, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]  # /id   /posts/{id} #prefix for all the routes in this router 
    
)
@router.get("/", response_model=list[schemas.PostOut])  #response_model is used to define the response schema and we get the list of posts
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_currents_user), limit: int = 10, skip: int = 0, search: Optional[str] = "" ):  #Post is a pydantic model
    
    #cursor.execute("""SELECT * FROM posts""")
    #posts = cursor.fetchall()
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()  #get the posts from the database
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, 
    isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return  posts





@router.get("/")
def get_posts():
    return {"data": "This is posts"}

#@app.post("/posts")
#def create_posts(payload: dict = Body(...)):
   # print(payload)
    #return {"new_post": f"title : {payload['title']} content: {payload['content']} "}

@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)  #response_model is used to define the response schema
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_currents_user)):  #Post is a pydantic model
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
                    # (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    #print(**post.dict()) it is to avoid writing all the fields below
    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
  
    new_post = models.Post(owner_id=current_user.id, **post.dict()) #**post.dict() is used to unpack the dictionary and pass it as keyword arguments
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #pydantic dont know how to work with sqlalchemy objects it only work with dict objects
    return new_post  #return {"data": new_post} #returning the new post - it was initially like this

@router.get("/{id}", response_model=schemas.PostOut)  #response_model is used to define the response schema
def get_post(id:int, response: Response, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_currents_user)):
    #cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    #post = cursor.fetchone()
    #post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, 
    isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    #
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_currents_user)):
    #cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    #deleted_post = cursor.fetchone()
    #conn.commit()

    deleted_post= db.query(models.Post).filter(models.Post.id == id).first()
    
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}", response_model=schemas.Post)  #response_model is used to define the response schema
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_currents_user)):
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #               (post.title, post.content, post.published, str(id)))
    #updated_post = cursor.fetchone()
    #conn.commit()

    updated_post = db.query(models.Post).filter(models.Post.id == id)
    
    if updated_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    if updated_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    
    updated_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return update_post