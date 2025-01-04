"""
Database connection settings
"""
import os
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def get_config_value(key):
    """Get configuration from either Streamlit secrets or environment variables"""
    try:
        return st.secrets.get(key) or os.getenv(key)
    except FileNotFoundError:
        return os.getenv(key)

required_env_vars = ['DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DATABASE']
missing_vars = [var for var in required_env_vars if not get_config_value(var)]

if missing_vars:
    raise EnvironmentError(
        f"As seguintes variáveis são obrigatórias e não foram encontradas: {', '.join(missing_vars)}"
    )

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
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    echo=False
)

__all__ = ['engine']
