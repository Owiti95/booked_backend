import pytest


def test_list_users(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.get('/admin/users', headers=headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_add_store_book(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.post('/admin/store_books', headers=headers, json={
        "title": "Test Book",
        "author": "Author Name",
        "genre": "Fiction",
        "isbn": "1234567890",
        "price": 10.99,
        "stock": 5
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test Book"


def test_update_store_book(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    client.post('/admin/store_books', headers=headers, json={
        "title": "Test Book",
        "author": "Author Name",
        "genre": "Fiction",
        "isbn": "1234567890",
        "price": 10.99,
        "stock": 5
    })
    response = client.put('/admin/store_books/1', headers=headers, json={
        "title": "Updated Title"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == "Updated Title"


def test_delete_store_book(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    client.post('/admin/store_books', headers=headers, json={
        "title": "Test Book",
        "author": "Author Name",
        "genre": "Fiction",
        "isbn": "1234567890",
        "price": 10.99,
        "stock": 5
    })
    response = client.delete('/admin/store_books/1', headers=headers)
    assert response.status_code == 200


def test_approve_order(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.post('/admin/approve_order/1', headers=headers, json={
        "action": "approve"
    })
    assert response.status_code == 404  # No sale exists yet
