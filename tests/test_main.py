from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json()["version"] == "0.0.1"

def test_costs_summary():
    mock_response = {
        "ResultsByTime": [{
            "Total": {
                "UnblendedCost": {
                    "Amount": "1.91",
                    "Unit": "USD"
                }
            }
        }]
    }
    with patch("app.costs.get_cost_client") as mock_client:
        mock_client.return_value.get_cost_and_usage.return_value = mock_response
        response = client.get("/costs/summary")
        assert response.status_code == 200
        assert "total_cost" in response.json()

def test_costs_breakdown():
    mock_response = {
        "ResultsByTime": [{
            "Groups": [{
                "Keys": ["Amazon S3"],
                "Metrics": {
                    "UnblendedCost": {
                        "Amount": "0.50",
                        "Unit": "USD"
                    }
                }
            }]
        }]
    }
    with patch("app.costs.get_cost_client") as mock_client:
        mock_client.return_value.get_cost_and_usage.return_value = mock_response
        response = client.get("/costs/breakdown")
        assert response.status_code == 200
        assert isinstance(response.json()["breakdown"], list)

def test_costs_history():
    mock_response = {
        "ResultsByTime": [{
            "TimePeriod": {"Start": "2026-08-01"},
            "Total": {
                "UnblendedCost": {
                    "Amount": "0.85",
                    "Unit": "USD"
                }
            }
        }]
    }
    with patch("app.costs.get_cost_client") as mock_client:
        mock_client.return_value.get_cost_and_usage.return_value = mock_response
        response = client.get("/costs/history")
        assert response.status_code == 200
        assert isinstance(response.json()["daily_costs"], list)