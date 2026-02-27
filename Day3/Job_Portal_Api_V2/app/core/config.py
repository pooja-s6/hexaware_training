#config.py

import os
from dotenv import load_dotenv

load_dotenv()

#Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/job_db")

#JWT Settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
