
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "it works !"}


@app.get("/addition")
def addition(a: int, b: int):
    return {
        "result a+b=": a + b,
        "developer": "Dev1"
    }
