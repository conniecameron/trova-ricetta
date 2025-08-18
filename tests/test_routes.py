import pytest
import json
from app.routes import *

@pytest.fixture
def client():
    a = create_app()
    with a.test_client() as client:
        yield client

def test_recipes_all_ok(client):
    rv = client.get("/recipes/all")
    assert rv.status_code == 200
    data = rv.get_json()
    assert len(data) == 5

def test_search_recipes_found(client):
    payload = {
        "meal_type": "dolce",
        "ingredients": ["uova", "farina", "latte"],
        "min_matches": 3
    }
    rv = client.post("/recipes/search", data=json.dumps(payload),
                     content_type="application/json")
    assert rv.status_code == 200
    data = rv.get_json()
    #assert "recipes" in data
    assert len(data) == 1
    assert data[0]["title"] == "Torta Margherita"
    # match_count should be >= 3 per our payload
    assert len(data[0]["ingredients"]) >= 3

def test_search_recipes_notfound(client):
    payload = {
        "meal_type": "dolce",
        "ingredients": ["uova", "farina", "nutella"],
        "min_matches": 3
    }
    rv = client.post("/recipes/search", data=json.dumps(payload),
                     content_type="application/json")
    assert rv.status_code == 404
    data = rv.get_json()





