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

def find_post_index(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

#Get all Posts
@app.get("/posts")
def get_posts():
    return {"data":my_posts}


#Create Post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = random.randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":my_posts}

#Get specific Post
@app.get("/posts/{id}")
def get_post(id:int):
    post = find_post(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} wasn't found")
        #response.status_code = 404
        #return {f"post with id: {id} wasn't found"}

    return {"post details":post}


#Delete Post
@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def get_post(id:int):
    index = find_post_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} id does not exist!!")
    
    my_posts.pop(index)
    return {"message":"Post deleted successfully"}

#Update Post
@app.put("/posts/{id}")
def update_post(id:int, post : Post):
    index = find_post_index(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} id does not exist!!")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data" : post_dict}