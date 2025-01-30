"""
Module to connect to the SQLite database
"""

import os
import streamlit as st
from sqlalchemy import create_engine, text

def init_db(engine):
    """Initialize database with init.sql"""
    with engine.connect() as conn:
        with open("customer_management/database/init.sql") as file:
            statements = file.read().split(';')
            for stmt in statements:
                if stmt.strip():
                    conn.execute(text(stmt.strip()))
            conn.commit()

def get_engine():
    """Get database engine based on environment"""
    if os.getenv('GITHUB_ACTIONS'):
        return create_engine('sqlite:///local_database.db')
    
    try:
        if st.secrets.get("postgres"):
            return create_engine(
                f"postgresql://{st.secrets.postgres.user}:{st.secrets.postgres.password}"
                f"@{st.secrets.postgres.host}:{st.secrets.postgres.port}/{st.secrets.postgres.dbname}"
            )
    except:
        pass
    
    return create_engine('sqlite:///local_database.db')

engine = get_engine()

if os.getenv('GITHUB_ACTIONS') or not os.path.exists('local_database.db'):
    init_db(engine)
