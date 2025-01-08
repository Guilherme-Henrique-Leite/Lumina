"""
Module to connect to the PostgreSQL database
"""

import os
import streamlit as st
from sqlalchemy import create_engine

def get_config(key: str) -> str:
    if hasattr(st, "secrets"):
        return st.secrets.get(key)
    return os.getenv(key)

DB_USER = get_config("DB_USER")
DB_PASSWORD = get_config("DB_PASSWORD")
DB_HOST = get_config("DB_HOST")
DB_PORT = get_config("DB_PORT")
DATABASE = get_config("DATABASE")

HANDLER_CONNECTION = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}?sslmode=require"

try:
    engine = create_engine(HANDLER_CONNECTION)
except Exception as e:
    print(f"Error connecting to database: {str(e)}")
