"""
Module to connect to the SQLite database
"""

import os
from sqlalchemy import create_engine, text
import streamlit as st

def init_db(engine):
    """Initialize database with init.sql"""
    with engine.connect() as conn:
        with open("customer_management/database/init.sql") as file:
            for stmt in file.read().split(';'):
                if stmt.strip():
                    conn.execute(text(stmt.strip()))
            conn.commit()

def get_engine():
    if st.secrets.get("postgres"):
        return create_engine(st.secrets.postgres.url)
    return create_engine("sqlite:///local.db")

# Inicialização do banco
engine = get_engine()
init_db(engine)
