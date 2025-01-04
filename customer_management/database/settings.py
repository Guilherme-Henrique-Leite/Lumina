"""
Database connection settings
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

required_env_vars = ['DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DATABASE']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    raise EnvironmentError(
        f"As seguintes variáveis de ambiente são obrigatórias e não foram encontradas: {', '.join(missing_vars)}"
    )

DB_CONFIG = {
    'drivername': 'postgresql',
    'username': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': int(os.getenv('DB_PORT')),
    'database': os.getenv('DATABASE')
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
