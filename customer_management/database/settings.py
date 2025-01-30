"""
Module to connect to the SQLite database
"""

import os
from sqlalchemy import create_engine, text
import logging

logger = logging.getLogger(__name__)

def get_database_url():
    """Get database URL from environment or use default SQLite"""
    return os.getenv('DATABASE_URL', 'sqlite:///customer_management.db')


engine = create_engine(get_database_url())

def get_connection():
    """Get database connection"""
    return engine.connect()

HANDLER_CONNECTION = get_connection

def init_db(engine):
    """Initialize database with schema and initial data"""
    with open('customer_management/database/init.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()
        
    with engine.connect() as conn:
        for stmt in sql_script.split(';'):
            if stmt.strip():
                conn.execute(text(stmt.strip()))
                conn.commit()

if not os.path.exists('customer_management.db'):
    init_db(engine)
