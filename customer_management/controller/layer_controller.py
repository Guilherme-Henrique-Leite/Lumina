"""
Module to run a data pipeline
"""

from customer_management.raw.bronze.bronze_layer import bronze_customers
from customer_management.raw.silver.silver_layer import silver_customers
from customer_management.raw.gold.gold_layer import gold_customers

from customer_management.logger_config import logger
import pandas as pd

def run_data_pipeline():
    """
    Executa o pipeline de dados completo
    """
    try:
        logger.info("Starting data pipeline...")
        
        df_bronze = bronze_customers()
        if df_bronze.empty:
            logger.error("Bronze layer returned empty DataFrame")
            return pd.DataFrame()
            
        df_silver = silver_customers(df_bronze)
        if df_silver.empty:
            logger.error("Silver layer returned empty DataFrame")
            return pd.DataFrame()
            
        df_gold = gold_customers(df_silver)
        
        logger.info("Pipeline completed successfully")
        return df_gold
        
    except Exception as e:
        logger.error(f"Error in pipeline: {e}")
        return pd.DataFrame()
