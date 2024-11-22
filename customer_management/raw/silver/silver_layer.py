"""
Module to transform data from the bronze layer to the silver layer.
"""

from customer_management.utils import (
    check_object,
    contains_emoji,
    optimize_memory,
    clean_and_validate_data,
)

def silver_customers(df_bronze):
    """
    Transforms raw customer data (Bronze layer) into a clean and optimized dataset.

    Args:
        df_bronze(pd.DataFrame): Raw data from the Bronze layer.

    Returns:
        pd.DataFrame: A transformed DataFrame ready for the Silver layer.
    """
    
    df_silver = clean_and_validate_data(df_bronze)
    
    df_silver['email_domain'] = df_silver['email'].apply(lambda x: x.split('@')[-1])
    
    object_columns = check_object(df_silver, df_silver.columns)
    df_silver = optimize_memory(df_silver, object_columns)
    
    df_silver = df_silver[~df_silver['name'].apply(contains_emoji)]
    
    return df_silver
