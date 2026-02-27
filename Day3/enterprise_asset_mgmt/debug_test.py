import sys
import os
import traceback
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.base import Base
from app.models import user, department, asset, asset_assignment, asset_request
from app.schemas.user_schema import UserCreate
from app.repositories.user_repo import UserRepository

# Setup test database
TEST_DATABASE_URL = "sqlite:///./test_debug.db"

# Remove existing database if it exists
if os.path.exists("test_debug.db"):
    try:
        os.remove("test_debug.db")
    except PermissionError:
        print("Warning: Could not remove existing test_debug.db - file may be in use")

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables
Base.metadata.create_all(bind=engine)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    db = TestingSessionLocal()
    user_repo = UserRepository(db)
    
    user_data = UserCreate(
        name="Test User",
        email="test@example.com",
        password="password123",
        role="EMPLOYEE"
    )
    
    user = user_repo.create_user(user_data)
    print(f"Success! Created user: {user.id}, {user.name}, {user.email}")
    
except Exception as e:
    print(f"Error: {type(e).__name__}: {str(e)}")
    traceback.print_exc()
    
finally:
    db.close()
    engine.dispose()  # Properly dispose of the engine
    
    # Clean up - give a moment for the file to be released
    import time
    time.sleep(0.1)
    
    if os.path.exists("test_debug.db"):
        try:
            os.remove("test_debug.db")
            print("Cleaned up test database")
        except PermissionError:
            print("Warning: Could not remove test_debug.db - file may still be in use")
