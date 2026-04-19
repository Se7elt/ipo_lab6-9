import requests

BASE_URL = "http://127.0.0.1:8000"


def test_mean():
    """Verify /mean endpoint returns expected average value."""
    response = requests.get(f"{BASE_URL}/mean?numbers=10,20,30")
    assert response.status_code == 200
    assert response.json()["result"] == 20.0


def test_factorial():
    """Verify /factorial endpoint returns expected factorial value."""
    response = requests.get(f"{BASE_URL}/factorial/5")
    assert response.status_code == 200
    assert response.json()["result"] == 120


def test_reverse():
    """Verify /reverse endpoint returns reversed text."""
    response = requests.get(f"{BASE_URL}/reverse?text=hello")
    assert response.status_code == 200
    assert response.json()["result"] == "olleh"
