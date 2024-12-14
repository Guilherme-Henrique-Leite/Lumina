"""
Module to extract data for the bronze layer
"""

import logging
import pandas as pd

from customer_management.database.settings import engine

logger = logging.getLogger(__name__)

def bronze_customers():
    """
    Extracts raw data from the customers table.
    """
    query = """
        SELECT 
            id,
            name,
            email,
            contact,
            country,
            city,
            neighborhood,
            created_at
        FROM customers
        ORDER BY created_at DESC
    """
    
    try:
        with engine.connect() as conn:
            df = pd.read_sql(query, conn)
            return df
    except Exception as e:
        logger.error(f"Error reading from database: {e}")
        return pd.DataFrame()
