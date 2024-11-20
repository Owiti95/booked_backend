import pytest


def test_register(client):
    response = client.post('/user/register', json={
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["email"] == "testuser@example.com"


def test_login(client):
    client.post('/user/register', json={
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "password123"
    })
    response = client.post('/user/login', json={
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert "access_token" in data


def test_view_store_books(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get('/user/store_books', headers=headers)
    assert response.status_code == 200


def test_view_library_books(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get('/user/library_books', headers=headers)
    assert response.status_code == 200


def test_search_books(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get('/user/search_books?query=fiction', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert "store_books" in data
    assert "library_books" in data


def test_add_to_cart(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.post('/user/add_to_cart', headers=headers, json={
        "book_id": 1,
        "quantity": 2
    })
    assert response.status_code == 400  # No books exist in the store


def test_view_cart(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get('/user/cart', headers=headers)
    assert response.status_code == 200
    assert response.get_json() == []


def test_checkout_empty_cart(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.post('/user/checkout', headers=headers)
    assert response.status_code == 400
    assert response.get_json()["error"] == "Your cart is empty"
