# Hiring Application Backend

## How to Run

1. Install dependencies: `pip install -r app/requirements.txt`
2. Configure database in `app/.env` file
3. Create database: `CREATE DATABASE hiring_db;`
4. Run migrations: `alembic upgrade head`
5. Start server: `cd app` then `uvicorn main:app --reload`
6. Access API docs: `http://localhost:8000/docs`
