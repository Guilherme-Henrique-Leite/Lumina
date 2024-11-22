"""
Module to extract data for the bronze layer
"""

import pandas as pd

from sqlalchemy import text

from customer_management.database import engine

def bronze_customers():
    """
    Extract data from the customers table and return it as a DataFrame.
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM customers"))
            df_customers = pd.DataFrame(result.fetchall(), columns=result.keys())
        return df_customers
    except Exception as e:
        print(f"Error extracting data for the bronze layer: {e}")
        return pd.DataFrame()
