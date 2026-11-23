from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}


def test_addition():
    response = client.get("/addition", params={"a": 3, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result a+b=": 8, "developer": "Dev1"}


def test_soustraction():
    response = client.get("/soustraction", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result a-b=": 6, "developer": "Dev1"}


def test_greeting():
    response = client.get("/greeting", params={"name": "Achwek"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, Achwek"
    assert data["developer"] == "Dev2"
    assert "hostname" in data
    assert "IP" in data


def test_multiply_get_and_post():
    res_get = client.get("/multiply", params={"a": 3, "b": 4})
    assert res_get.status_code == 200
    assert res_get.json() == {"result a*b=": 12, "developer": "Dev1"}

    res_post = client.post("/multiply", params={"a": 2, "b": 5})
    assert res_post.status_code == 200
    assert res_post.json() == {"result a*b=": 10, "developer": "Dev1"}


def test_divide_normal_and_zero():
    res_ok = client.post("/divide", params={"a": 10, "b": 2})
    assert res_ok.status_code == 200
    assert res_ok.json() == {"result a/b=": 5.0, "developer": "Dev2"}

    res_zero = client.post("/divide", params={"a": 10, "b": 0})
    assert res_zero.status_code == 200
    assert res_zero.json() == {"error": "Division par zéro impossible"}