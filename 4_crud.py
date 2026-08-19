from typing import Optional
from fastapi import FastAPI, Response, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
import random

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1",
             "content":"content of post 1",
             "id":1},
            {"title":"title of post 2",
             "content":"content of post 2",
             "id":2}]

def find_post(id):
    for i in my_posts:
        if i['id'] == id:
            return i

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = random.randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":my_posts}

@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} wasn't found")
        #response.status_code = 404
        #return {f"post with id: {id} wasn't found"}

    return {"post details":post}
