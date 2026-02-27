#test_candidate.py

def test_get_all_jobs(client):
    #Create an employer and job first
    client.post("/auth/register", json={
        "username": "emp", "email": "emp@test.com",
        "role": "employer", "password": "pass123"
    })
    emp_login = client.post("/auth/login", json={
        "email": "emp@test.com", "password": "pass123"
    })
    emp_token = emp_login.json()["access_token"]
    
    client.post("/employer/jobs",
        json={"title": "Job1", "description": "Test", "salary": 50000, "company_id": 1},
        headers={"Authorization": f"Bearer {emp_token}"}
    )
    
    #Get all jobs (no auth needed)
    response = client.get("/candidate/jobs")
    assert response.status_code == 200

def test_apply_to_job(client):
    #Create employer and job
    client.post("/auth/register", json={
        "username": "emp", "email": "emp2@test.com",
        "role": "employer", "password": "pass123"
    })
    emp_login = client.post("/auth/login", json={
        "email": "emp2@test.com", "password": "pass123"
    })
    emp_token = emp_login.json()["access_token"]
    
    job = client.post("/employer/jobs",
        json={"title": "Job", "description": "Test", "salary": 50000, "company_id": 1},
        headers={"Authorization": f"Bearer {emp_token}"}
    )
    job_id = job.json()["id"]
    
    #Register candidate
    client.post("/auth/register", json={
        "username": "cand", "email": "cand@test.com",
        "role": "candidate", "password": "pass123"
    })
    cand_login = client.post("/auth/login", json={
        "email": "cand@test.com", "password": "pass123"
    })
    cand_token = cand_login.json()["access_token"]
    
    #Apply to job
    response = client.post("/candidate/applications",
        json={"job_id": job_id},
        headers={"Authorization": f"Bearer {cand_token}"}
    )
    assert response.status_code == 200

def test_get_my_applications(client):
    #Register candidate
    client.post("/auth/register", json={
        "username": "cand2", "email": "cand2@test.com",
        "role": "candidate", "password": "pass123"
    })
    cand_login = client.post("/auth/login", json={
        "email": "cand2@test.com", "password": "pass123"
    })
    cand_token = cand_login.json()["access_token"]
    
    #Get applications
    response = client.get("/candidate/applications",
        headers={"Authorization": f"Bearer {cand_token}"}
    )
    assert response.status_code == 200
