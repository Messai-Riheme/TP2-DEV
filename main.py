"""API FastAPI pour les opérations arithmétiques et informations système."""

import socket
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    """Retourne un message de bienvenue."""
    return {"message": "it works !"}


@app.get("/addition")
def addition(a: int, b: int):
    """Retourne la somme de deux entiers."""
    return {
        "result a+b=": a + b,
        "developer": "Dev1",
    }


@app.get("/soustraction")
def soustraction(a: int, b: int):
    """Retourne la différence de deux entiers."""
    return {
        "result a-b=": a - b,
        "developer": "Dev1",
    }


@app.get("/greeting")
def greeting(name: str):
    """Retourne un message de salutation avec le nom d'hôte et l'adresse IP."""
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_address = "127.0.0.1"

    return {
        "message": f"Hello, {name}",
        "developer": "Dev2",
        "hostname": hostname,
        "IP": ip_address,
    }


@app.get("/multiply")
@app.post("/multiply")
def multiply(a: int = 0, b: int = 0):
    """Retourne le produit de deux entiers."""
    return {
        "result a*b=": a * b,
        "developer": "Dev1",
    }


@app.post("/divide")
def divide(a: float, b: float):
    """Retourne le quotient de deux flottants ou un message d'erreur si b vaut 0."""
    if b == 0:
        return {"error": "Division par zéro impossible"}
    return {
        "result a/b=": a / b,
        "developer": "Dev2",
    }