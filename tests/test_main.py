from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={
        "name": "Laptop",
        "description": "A high-performance laptop.",
        "price": 1500.0,
        "quantity": 10
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Laptop"
    assert response.json()["description"] == "A high-performance laptop."
    assert response.json()["price"] == 1500.0
    assert response.json()["quantity"] == 10


def test_get_all_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"
    assert response.json()["price"] == 1500.0
