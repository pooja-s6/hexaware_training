#test_employer.py

def test_create_job(client):
    #Register employer
    client.post("/auth/register", json={
        "username": "emp1", "email": "emp@test.com", 
        "role": "employer", "password": "pass123"
    })
    
    #Login
    login = client.post("/auth/login", json={
        "email": "emp@test.com", "password": "pass123"
    })
    token = login.json()["access_token"]
    
    #Create job
    response = client.post("/employer/jobs", 
        json={"title": "Developer", "description": "Test", "salary": 50000, "company_id": 1},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

def test_get_my_jobs(client):
    #Register and login
    client.post("/auth/register", json={
        "username": "emp2", "email": "emp2@test.com",
        "role": "employer", "password": "pass123"
    })
    login = client.post("/auth/login", json={
        "email": "emp2@test.com", "password": "pass123"
    })
    token = login.json()["access_token"]
    
    #Get jobs
    response = client.get("/employer/jobs",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200