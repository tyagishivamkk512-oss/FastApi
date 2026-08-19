from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Welcome to my first FastAPI project"}

#from this we get url1
#if we change @app.get("/") to @app.get("/login") we will get another url
# or we can continue to login with url1 but at last we have to change the url to url1/login
#same with @app.get("/login") we can change it to @app.get("/login/username") and we will get url1/login/username
#or any other path we want to add to the url

@app.get("/login")
def login():
    return {"message": "This is the login page"}