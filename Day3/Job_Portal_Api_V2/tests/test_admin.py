#test_admin.py

def test_get_all_users(client):
    #Register admin
    client.post("/auth/register", json={
        "username": "admin", "email": "admin@test.com",
        "role": "admin", "password": "pass123"
    })
    admin_login = client.post("/auth/login", json={
        "email": "admin@test.com", "password": "pass123"
    })
    admin_token = admin_login.json()["access_token"]
    
    #Get all users
    response = client.get("/admin/users",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200

def test_create_company(client):
    #Register admin
    client.post("/auth/register", json={
        "username": "admin2", "email": "admin2@test.com",
        "role": "admin", "password": "pass123"
    })
    admin_login = client.post("/auth/login", json={
        "email": "admin2@test.com", "password": "pass123"
    })
    admin_token = admin_login.json()["access_token"]
    
    #Create company
    response = client.post("/admin/companies",
        json={"name": "Tech Corp", "description": "IT Company"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200

def test_get_all_companies(client):
    #Register admin
    client.post("/auth/register", json={
        "username": "admin3", "email": "admin3@test.com",
        "role": "admin", "password": "pass123"
    })
    admin_login = client.post("/auth/login", json={
        "email": "admin3@test.com", "password": "pass123"
    })
    admin_token = admin_login.json()["access_token"]
    
    #Get companies
    response = client.get("/admin/companies",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
