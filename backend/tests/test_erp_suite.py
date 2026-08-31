import pytest
from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

client = TestClient(app)

def test_erp_health_and_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()["status"] == "Online"

def test_admin_authentication():
    res = client.post("/api/auth/login", json={"email": "admin@collexa.edu", "password": "admin123"})
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["user"]["role"] == "ADMIN"

def test_student_flow():
    login_res = client.post("/api/auth/login", json={"email": "student@collexa.edu", "password": "student123"})
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Test books catalog
    books_res = client.get("/api/library/books", headers=headers)
    assert books_res.status_code == 200
    assert len(books_res.json()) >= 1

    # Test campus events
    events_res = client.get("/api/events/", headers=headers)
    assert events_res.status_code == 200
    assert len(events_res.json()) >= 1

    # Test placement drives
    drives_res = client.get("/api/placements/drives", headers=headers)
    assert drives_res.status_code == 200
    assert len(drives_res.json()) >= 1

    # Test chat channels
    channels_res = client.get("/api/chat/channels", headers=headers)
    assert channels_res.status_code == 200
    assert len(channels_res.json()) >= 1

def test_ai_advisor():
    login_res = client.post("/api/auth/login", json={"email": "student@collexa.edu", "password": "student123"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    res = client.post("/api/ai/assistant/query", json={"query": "attendance criteria"}, headers=headers)
    assert res.status_code == 200
    assert "attendance" in res.json()["answer"].lower()

def test_hostel_and_bus_routes():
    login_res = client.post("/api/auth/login", json={"email": "student@collexa.edu", "password": "student123"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    h_res = client.get("/api/hostel-transport/hostels", headers=headers)
    assert h_res.status_code == 200
    assert len(h_res.json()) >= 1

    b_res = client.get("/api/hostel-transport/bus-routes", headers=headers)
    assert b_res.status_code == 200
    assert len(b_res.json()) >= 1
