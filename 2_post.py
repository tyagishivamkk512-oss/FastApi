from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/post")
def get_post():
    return {"message": "This is the post"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title is {payload['title']} and content is {payload['content']}"}

