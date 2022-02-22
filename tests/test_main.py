from fastapi.testclient import TestClient

from emptycabinet.main import app
from emptycabinet.routers import products

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_products_endpoint():
    response = client.get("/api/products")
    assert response.status_code == 200
    assert response.json() == {"Products": products.product_list}
