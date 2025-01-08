"""
Module to connect to the PostgreSQL database
"""

import os
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


def get_config(key: str) -> str:
    if hasattr(st, "secrets"):
        return st.secrets.get(key)
    return os.getenv(key)

DB_HOST = get_config("DB_HOST")
DB_USER = get_config("DB_USER")
DB_PASS = get_config("DB_PASSWORD")
DB_NAME = get_config("DATABASE")
DB_PORT = get_config("DB_PORT")

HANDLER_CONNECTION = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

try:
    engine = create_engine(HANDLER_CONNECTION)
except OperationalError as e:
    print(f"Error to connect a PostgreSQL: {e}")
except Exception as e:
    print(f"Unexpected error to connect a database: {e}")
