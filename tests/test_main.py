from fastapi.testclient import TestClient 
from app.main import app

client = TestClient (app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"]=="healthy"



def test_version():
     response = client.get("/version")
     assert response.status_code == 200
     assert response.json()["version"]=="0.0.1"


def test_costs_summary():
     response = client.get("/costs/summary")
     assert response.status_code == 200
     assert "total_cost" in response.json()


def test_costs_breakdown():
     response = client.get("/costs/breakdown")
     assert response.status_code == 200
     assert isinstance (response.json()["breakdown"], list)


def test_costs_history():
     response = client.get("/costs/history")
     assert response.status_code == 200
     assert isinstance (response.json()["daily_costs"], list)