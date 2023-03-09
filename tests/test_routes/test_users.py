import json


def test_create_user(client):
    data = {
        "username": "cezar@rocha",
        "email": "cezar.rocha@gmail.com",
        "password": "testeteste",
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@teste.com"
    assert response.json()["is_active"] == True
