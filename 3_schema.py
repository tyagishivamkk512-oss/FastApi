from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
def get_post():
    return {"message": "This is the post page"}

@app.post("/createpost")
def create_post(meri_post: Post):
    print(meri_post.published)
    print(meri_post.title)
    print(meri_post.rating)
    print(meri_post.dict())

    return {"title": meri_post.title, "content": meri_post.content}