"""
Database connection settings
"""
import os
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL



def get_config_value(key):
    """Get configuration from either Streamlit secrets or environment variables"""
    try:
        value = st.secrets.get(key) or os.getenv(key)
        return value
    except FileNotFoundError:
        return os.getenv(key)

DB_CONFIG = {
    'drivername': 'postgresql',
    'username': get_config_value('DB_USER'),
    'password': get_config_value('DB_PASSWORD'),
    'host': get_config_value('DB_HOST'),
    'port': int(get_config_value('DB_PORT')),
    'database': get_config_value('DATABASE')
}

connection_url = URL.create(**DB_CONFIG)

engine = create_engine(
    connection_url,
    pool_size=1,
    max_overflow=2,
    pool_timeout=5,
    pool_recycle=300,
    connect_args={
        'connect_timeout': 5,
        'application_name': 'lumina_app'
    }
)

def test_connection():
    """Test database connection with timeout"""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return True
    except Exception as e:
        return False

if not test_connection():
    raise Exception("Falha no teste inicial de conexão!")

__all__ = ['engine', 'test_connection']
