from fastapi import FastAPI
from . import models

from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origin = ["http://www.google.com"]  # Add your frontend URL here

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(post.router)  #to include the post router
app.include_router(user.router)  #to include the user router
app.include_router(auth.router)  #to include the auth router
app.include_router(vote.router)  #to include the vote router

@app.get("/")
async def root():
    return {"message": "Hello World"}



























#----------------------------------------------------------------------------------------------------------------------------#

#as we dont want to expose the response/info to the user that they already know

#-----------------------------------------------------------------------------------------------------------------------------#



#while True:
    #try:
        #conn = psycopg2.connect(host='localhost', database='fastapi', user='shifatazeenshaikh', 
        # password='shifa123', cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print("Database connection was successful")
        #break
        #except Exception as error:
        #print("Connecting to database failed")
        #print("Error: ", error)
        #time.sleep(2)  #wait for 2 seconds before trying to connect again
#my_posts = [{"title": "printer", "content": "very expensive printer", "id": 1},{
    #"title": "laptop", "content": "very expensive laptop", "id": 2}]
# def find_post(id):
#     for post in my_posts:
#         if post['id'] == id:
#             return post

# def find_post_index(id):
#     for i, post in enumerate(my_posts):
#         if post['id'] == id:
#             return i


#@app.get("/sqlalchemy")    test-route to test sqlalchemy
#def test_post(db: Session = Depends(get_db)):
    #posts = db.query(models.Post).all()
    #print(posts)
    #return {"data": "success"}
