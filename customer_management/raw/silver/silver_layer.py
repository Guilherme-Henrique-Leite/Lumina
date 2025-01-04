"""
Module to transform data from the bronze layer to the silver layer.
"""

import re
import logging
import pandas as pd
from customer_management.utils import (
    check_object,
    contains_emoji,
    optimize_memory,
    clean_and_validate_data,
)

logger = logging.getLogger(__name__)
def silver_customers(df_bronze):
    """
    Processa os dados da camada bronze para silver
    """
    logger.info("Processing Silver layer...")
    
    df_silver = df_bronze.copy()
    
    df_silver['email_domain'] = df_silver['email'].apply(lambda x: x.split('@')[-1] if pd.notna(x) else None)
    
    df_silver['contact'] = df_silver['contact'].apply(lambda x: re.sub(r'\D', '', str(x)) if pd.notna(x) else None)
    
    text_columns = ['name', 'email', 'country', 'state', 'city', 'neighborhood']
    for col in text_columns:
        if col in df_silver.columns:
            df_silver[col] = df_silver[col].apply(lambda x: x.strip().title() if isinstance(x, str) else x)
    
    logger.info("Silver layer completed.")
    return df_silver
