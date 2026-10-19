import socket
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

@app.get("/greeting")
def greeting(name: str):
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except Exception:
        ip_address = "127.0.0.1"

    return {
        "message": f"Hello, {name}",
        "developer": "Dev1",
        "hostname": hostname,
        "IP": ip_address
    }