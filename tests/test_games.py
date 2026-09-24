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


def test_filter_games_by_platform():
    response = client.get("/games/?platform=PS5")

    assert response.status_code == 200

    data = response.json()

    for game in data:
        assert game["platform"] == "PS5"


def test_filter_games_by_min_price():
    response = client.get("/games/?min_price=100")

    assert response.status_code == 200

    data = response.json()

    for game in data:
        assert game["purchase_price"] >= 100


def test_filter_games_by_max_price():
    response = client.get("/games/?max_price=200")

    assert response.status_code == 200

    data = response.json()

    for game in data:
        assert game["purchase_price"] <= 200


def test_update_game():
    create_response = client.post(
        "/games/",
        json={
            "name": "Resident Evil 4",
            "platform": "PS2",
            "purchase_price": 50,
            "sale_price": 100
        }
    )

    game_id = create_response.json()["id"]

    response = client.put(
        f"/games/{game_id}",
        json={
            "sale_price": 130
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == game_id
    assert data["name"] == "Resident Evil 4"
    assert data["purchase_price"] == 50
    assert data["sale_price"] == 130


def test_sell_game():
    create_response = client.post(
        "/games/",
        json={
            "name": "Gran Turismo 4",
            "platform": "PS2",
            "purchase_price": 30,
            "sale_price": 80
        }
    )

    assert create_response.status_code == 201

    game_id = create_response.json()["id"]

    response = client.post(
        f"/games/{game_id}/sell"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == game_id
    assert data["status"] == "sold"


def test_sell_game_twice():
    create_response = client.post(
        "/games/",
        json={
            "name": "God of War II",
            "platform": "PS2",
            "purchase_price": 40,
            "sale_price": 90
        }
    )

    assert create_response.status_code == 201

    game_id = create_response.json()["id"]

    first_sale = client.post(
        f"/games/{game_id}/sell"
    )

    assert first_sale.status_code == 200

    second_sale = client.post(
        f"/games/{game_id}/sell"
    )

    assert second_sale.status_code == 400
    assert second_sale.json()["detail"] == "Game already sold"