"""
Module to connect to the PostgreSQL database
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DATABASE")

HANDLER_CONNECTION = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}"

try:
    engine = create_engine(HANDLER_CONNECTION)
    connection = engine.connect()
    connection.close()
except OperationalError as e:
    print(f"Error to connect a PostgreSQL: {e}")
except Exception as e:
    print(f"Unexpected error to connect a database: {e}")
