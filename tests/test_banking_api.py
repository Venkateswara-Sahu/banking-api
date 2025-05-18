import requests

BASE_URL = "http://localhost:5000/api"

def test_get_balance():
    response = requests.get(f"{BASE_URL}/balance")
    assert response.status_code == 200
    data = response.json()
    assert "balance" in data
    assert isinstance(data["balance"], (int, float))

def test_deposit_valid():
    response = requests.post(f"{BASE_URL}/deposit", json={"amount": 1000})
    assert response.status_code == 200
    assert "message" in response.json()

def test_deposit_invalid_negative():
    response = requests.post(f"{BASE_URL}/deposit", json={"amount": -500})
    assert response.status_code == 400
    assert "error" in response.json()

def test_deposit_invalid_missing():
    response = requests.post(f"{BASE_URL}/deposit", json={})
    assert response.status_code == 400
    assert "error" in response.json()

def test_withdraw_valid():
    response = requests.post(f"{BASE_URL}/withdraw", json={"amount": 1000})
    assert response.status_code == 200
    assert "message" in response.json()

def test_withdraw_insufficient_balance():
    response = requests.post(f"{BASE_URL}/withdraw", json={"amount": 6000})
    assert response.status_code == 400
    assert "error" in response.json()

def test_withdraw_invalid_negative():
    response = requests.post(f"{BASE_URL}/withdraw", json={"amount": -100})
    assert response.status_code == 400
    assert "error" in response.json()

def test_withdraw_invalid_missing():
    response = requests.post(f"{BASE_URL}/withdraw", json={})
    assert response.status_code == 400
    assert "error" in response.json()


def test_create_account_valid():
    payload = {"name": "Alice", "balance": 1500}
    response = requests.post(f"{BASE_URL}/accounts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"
    assert data["balance"] == 1500
    assert "id" in data

def test_create_account_invalid():
    payload = {"name": "", "balance": -100}
    response = requests.post(f"{BASE_URL}/accounts", json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "error" in data

