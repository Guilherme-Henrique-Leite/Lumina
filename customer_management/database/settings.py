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

HANDLER_CONNECTION = "postgresql+psycopg2://admin:admin@172.17.0.1:5432/customers_db"


try:
    engine = create_engine(HANDLER_CONNECTION)
    connection = engine.connect()
    print("Connection successfully!")
    connection.close()
except OperationalError as e:
    print(f"Error to connect a PostgreSQL: {e}")
except Exception as e:
    print(f"Unexpected error to connect a database: {e}")
