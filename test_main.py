"""Tests unitaires pour l'application FastAPI."""

from fastapi.testclient import TestClient
from main import app

CLIENT = TestClient(app)


def test_home():
    """Teste la route racine."""
    response = CLIENT.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}


def test_addition():
    """Teste l'endpoint d'addition."""
    response = CLIENT.get("/addition", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {
        "result a+b=": 8,
        "developer": "Dev1",
    }


def test_soustraction():
    """Teste l'endpoint de soustraction."""
    response = CLIENT.get("/soustraction", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {
        "result a-b=": 6,
        "developer": "Dev1",
    }


def test_greeting():
    """Teste l'endpoint greeting."""
    response = CLIENT.get("/greeting", params={"name": "Rihem"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, Rihem"
    assert data["developer"] == "Dev2"
    assert "hostname" in data
    assert "IP" in data


def test_multiply_get_and_post():
    """Teste l'endpoint multiply en GET et en POST."""
    response_get = CLIENT.get("/multiply", params={"a": 3, "b": 4})
    assert response_get.status_code == 200
    assert response_get.json() == {
        "result a*b=": 12,
        "developer": "Dev1",
    }

    response_post = CLIENT.post("/multiply", params={"a": 2, "b": 5})
    assert response_post.status_code == 200
    assert response_post.json() == {
        "result a*b=": 10,
        "developer": "Dev1",
    }


def test_divide_success():
    """Teste la division de deux nombres avec un diviseur non nul."""
    response = CLIENT.post("/divide", params={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {
        "result a/b=": 5.0,
        "developer": "Dev2",
    }


def test_divide_by_zero():
    """Teste le cas de la division par zéro."""
    response = CLIENT.post("/divide", params={"a": 10, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Division par zéro impossible"}
