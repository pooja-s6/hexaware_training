#test_auth.py

def test_register_user(client):
    response = client.post("/auth/register", json={
        "username": "user1",
        "email": "user1@test.com",
        "role": "candidate",
        "password": "pass123"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "user1@test.com"

def test_login_success(client):
    #Register
    client.post("/auth/register", json={
        "username": "user2",
        "email": "user2@test.com",
        "role": "employer",
        "password": "pass123"
    })
    
    #Login
    response = client.post("/auth/login", json={
        "email": "user2@test.com",
        "password": "pass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid(client):
    response = client.post("/auth/login", json={
        "email": "wrong@test.com",
        "password": "wrong"
    })
    assert response.status_code == 401
