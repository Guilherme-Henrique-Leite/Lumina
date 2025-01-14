"""
Module to connect to the PostgreSQL database
"""

import os
import streamlit as st
from sqlalchemy import create_engine

def get_connection_string() -> str:
    if hasattr(st, "secrets"):
        return st.secrets["NEON_DATABASE_URL"]
    return os.getenv("NEON_DATABASE_URL")

try:
    HANDLER_CONNECTION = get_connection_string()
    engine = create_engine(HANDLER_CONNECTION)
except Exception as e:
    print(f"Error connecting to database: {str(e)}")
