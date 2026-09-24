from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "GameVault API"


def test_create_game():
    response = client.post(
        "/games/",
        json={
            "name": "God of War III",
            "platform": "PS3",
            "purchase_price": 40,
            "sale_price": 90
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "God of War III"
    assert data["platform"] == "PS3"
    assert data["purchase_price"] == 40
    assert data["sale_price"] == 90
    assert data["status"] == "available"


def test_list_games():
    response = client.get("/games/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_dashboard():
    response = client.get("/games/dashboard/summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_items" in data
    assert "inventory_cost" in data
    assert "potential_revenue" in data
    assert "potential_profit" in data
    assert "sold_items" in data