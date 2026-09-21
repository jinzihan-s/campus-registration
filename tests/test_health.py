import os
 
os.environ["SKIP_DB"] = "true"
 
from fastapi.testclient import TestClient
from app.main import app
 
 
def test_health():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
 
 
def test_index_returns_html_page():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.headers["content-type"].startswith("text/html")
        assert "校园活动报名" in response.text
