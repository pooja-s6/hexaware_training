# Hiring Application Backend - Enterprise Architecture

## Overview
The Hiring Application is an enterprise-grade backend system designed to manage job postings, user accounts, and job applications with a focus on scalability, maintainability, and production readiness.

## Features
- ✅ User Management (Admin, Recruiter, Candidate roles)
- ✅ Job Posting Management
- ✅ Job Application Tracking
- ✅ Role-Based Access Control
- ✅ Application Status Management (Applied, Shortlisted, Rejected)
- ✅ Pagination Support for Large Datasets
- ✅ Password Hashing for Security
- ✅ Transaction Management with Rollback
- ✅ Custom Exception Handling
- ✅ Request/Response Logging
- ✅ CORS Support

## Architecture

### Layered Architecture (Separation of Concerns)
```
Client → Controller (API) → Service (Business Logic) → Repository (DB Operations) → PostgreSQL
```

### Technology Stack
- **Framework**: FastAPI
- **ORM**: SQLAlchemy 2.0
- **Database**: PostgreSQL
- **Password Hashing**: Passlib with bcrypt
- **Migrations**: Alembic
- **Validation**: Pydantic

## Database Schema

### Tables
1. **Users** - User accounts with roles (admin, recruiter, candidate)
2. **Jobs** - Job postings with company information
3. **Applications** - Job applications linking users to jobs

### Relationships
- User (1) → (Many) Applications
- Job (1) → (Many) Applications
- Application (Many) → (1) User
- Application (Many) → (1) Job

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Virtual Environment

### Steps

1. **Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

2. **Install dependencies**
```bash
cd Day2/Hiring_app/app
pip install -r requirements.txt
```

3. **Setup PostgreSQL Database**
```sql
CREATE DATABASE hiring_db;
```

4. **Configure environment variables**
Edit `app/.env` file with your database credentials:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hiring_db
DB_USER=postgres
DB_PASSWORD=your_password
```

5. **Run database migrations (Optional - using Alembic)**
```bash
cd ..
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

6. **Run the application**
```bash
cd app
python main.py
```
Or using uvicorn:
```bash
uvicorn main:app --reload
```

## API Documentation

Once the application is running, access the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Users
- `POST /users/` - Create a new user
- `GET /users/` - List all users (with pagination)
- `GET /users/{user_id}` - Get user by ID
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

### Jobs
- `POST /jobs/` - Create a new job
- `GET /jobs/` - List all jobs (with pagination)
- `GET /jobs/{job_id}` - Get job by ID
- `PUT /jobs/{job_id}` - Update job
- `DELETE /jobs/{job_id}` - Delete job

### Applications
- `POST /applications/` - Apply for a job
- `GET /applications/` - List all applications (with pagination)
- `GET /applications/{application_id}` - Get application by ID
- `GET /applications/user/{user_id}` - Get all applications for a user
- `GET /applications/job/{job_id}` - Get all applications for a job
- `PATCH /applications/{application_id}/status` - Update application status
- `DELETE /applications/{application_id}` - Delete application

## Example Usage

### Create a User
```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "role": "candidate",
    "password": "securepassword123"
  }'
```

### Create a Job
```bash
curl -X POST "http://localhost:8000/jobs/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Backend Developer",
    "description": "FastAPI + PostgreSQL experience required",
    "salary": 120000,
    "company_id": 1
  }'
```

### Apply for a Job
```bash
curl -X POST "http://localhost:8000/applications/" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "job_id": 1
  }'
```

### List Jobs with Pagination
```bash
curl "http://localhost:8000/jobs/?skip=0&limit=10"
```

## Project Structure
```
Hiring_app/
├── app/
│   ├── main.py                 # Application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables
│   │
│   ├── core/                   # Core configurations
│   │   ├── config.py          # Settings and configuration
│   │   ├── database.py        # Database setup
│   │   └── logger.py          # Logging configuration
│   │
│   ├── models/                 # SQLAlchemy models
│   │   ├── base.py            # Base model imports
│   │   ├── user.py            # User model
│   │   ├── job.py             # Job model
│   │   └── application.py     # Application model
│   │
│   ├── schemas/                # Pydantic schemas
│   │   ├── user_schema.py     # User request/response schemas
│   │   ├── job_schema.py      # Job request/response schemas
│   │   └── application_schema.py
│   │
│   ├── repositories/           # Database operations
│   │   ├── user_repository.py
│   │   ├── job_repository.py
│   │   └── application_repository.py
│   │
│   ├── services/               # Business logic
│   │   ├── user_service.py
│   │   ├── job_service.py
│   │   └── application_service.py
│   │
│   ├── controllers/            # API endpoints
│   │   ├── user_controller.py
│   │   ├── job_controller.py
│   │   └── application_controller.py
│   │
│   ├── middleware/             # Middleware
│   │   ├── cors.py            # CORS configuration
│   │   └── logging.py         # Request logging
│   │
│   └── exceptions/             # Exception handling
│       ├── custom_exception.py
│       └── exception_handlers.py
│
├── alembic/                    # Database migrations
└── alembic.ini                 # Alembic configuration
```

## Development Notes

### Password Security
- Passwords are hashed using bcrypt
- Never store plain text passwords
- Hashed passwords are stored in the `hashed_password` field

### Error Handling
- Custom exceptions for domain-specific errors
- Global exception middleware catches unhandled errors
- Consistent JSON error responses

### Logging
- All requests are logged with execution time
- Logs are written to both console and file (`hiring_app.log`)
- Log level: INFO

### Data Validation
- Pydantic schemas validate all input/output
- Email validation using EmailStr
- Role and status validation using Enums

## Future Enhancements
- JWT Authentication
- Role-based authorization middleware
- Email notifications for application status changes
- Resume upload functionality
- Advanced search and filtering
- Rate limiting
- Caching with Redis
- Unit and integration tests
- Docker containerization
- CI/CD pipeline

## License
Enterprise Training Project - Hexaware Technologies

## Author
Developed as part of FastAPI Enterprise Architecture Training
