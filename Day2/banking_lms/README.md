# Banking Loan Management System (LMS)

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Configure database in `app/.env` file
3. Create database: `createdb banking_lms_db`
4. Run migrations: `alembic upgrade head`
5. Start server: `uvicorn app.main:app --reload`
6. Access API docs: `http://127.0.0.1:8000/docs`
7. Run tests: `pytest tests/`
