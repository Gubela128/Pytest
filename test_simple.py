import requests
import pytest

# Helper function to register an API client and get the access token
def get_access_token():
    client_data = {
        "clientName": "Nikoloz",
        "clientEmail": "your.email@example.com"
    }

    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=client_data)

    if response.status_code == 201:
        return response.json()["accessToken"]
    else:
        raise Exception("Failed to get access token. Status code: {response.status_code}")

# Use a fixture to get the access token before running tests
@pytest.fixture
def access_token():
    return get_access_token()

# Test the /status endpoint
def test_get_status():
    response = requests.get("https://simple-books-api.glitch.me/status")
    assert response.status_code == 200

# Test the /books endpoint
def test_get_books():
    response = requests.get("https://simple-books-api.glitch.me/books")
    assert response.status_code == 200

# Add more test cases for other endpoints as needed
