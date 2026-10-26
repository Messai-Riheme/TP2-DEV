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
        "developer": "Dev2",
        "hostname": hostname,
        "IP": ip_address
    }
@app.post("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division par zéro impossible"}
    return {
        "result a/b=": a / b,
        "developer": "Dev2"
    }