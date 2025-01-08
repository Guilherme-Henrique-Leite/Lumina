"""
Module to connect to the PostgreSQL database
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DATABASE")
DB_PORT = os.getenv("DB_PORT", "5432")

HANDLER_CONNECTION = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(HANDLER_CONNECTION)
except OperationalError as e:
    print(f"Error to connect a PostgreSQL: {e}")
except Exception as e:
    print(f"Unexpected error to connect a database: {e}")
