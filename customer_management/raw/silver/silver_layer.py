"""
Module to transform data from the bronze layer to the silver layer.
"""

from customer_management.raw import bronze_customers

from customer_management.utils import (
    check_object,
    contains_emoji,
    optimize_memory,
    clean_and_validate_data,
)

def silver_customers():
    """
    Transforms raw customer data (Bronze layer) into a clean and optimized dataset.

    Returns:
        pd.DataFrame: A transformed DataFrame ready for the Silver layer.
    """
    
    df_silver = bronze_customers()
    df_silver = clean_and_validate_data(df_silver)
    
    df_silver['email_domain'] = df_silver['email'].apply(lambda x: x.split('@')[-1])
    
    object_columns = check_object(df_silver, df_silver.columns)
    df_silver = optimize_memory(df_silver, object_columns)
    
    df_silver = df_silver[~df_silver['name'].apply(contains_emoji)]
    
    return df_silver

if __name__ == "__main__":
    df_silver = silver_customers()