
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
    # Récupérer le nom de la machine (hostname)
    hostname = socket.gethostname()

    # Récupérer l'adresse IP locale connectée au réseau
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = "127.0.0.1"
    finally:
        s.close()

    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "IP": ip_address
    }