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
            NULLIF(TRIM(country), '') as country,
            NULLIF(TRIM(state), '') as state,
            NULLIF(TRIM(city), '') as city,
            NULLIF(TRIM(neighborhood), '') as neighborhood,
            created_at
        FROM customers
        WHERE name != 'SYSTEM_LOCATION'  -- Exclui registros do sistema
        ORDER BY created_at DESC
    """
    
    try:
        with engine.connect() as conn:
            df = pd.read_sql(query, conn)
            return df
    except Exception as e:
        logger.error(f"Error reading from database: {e}")
        return pd.DataFrame()
