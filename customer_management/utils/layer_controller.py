"""
Module to run a data pipeline
"""

from customer_management.raw.bronze.bronze_layer import bronze_customers
from customer_management.raw.silver.silver_layer import silver_customers
from customer_management.raw.gold.gold_layer import gold_customers

from customer_management.logger_config import logger

def run_data_pipeline():
    """
    Executes the data pipeline from Bronze → Silver → Gold.
    """
    logger.info("Starting data pipeline...")

    logger.info("Processing Bronze layer...")
    df_bronze = bronze_customers()
    logger.info("Bronze layer completed.")

    logger.info("Processing Silver layer...")
    df_silver = silver_customers(df_bronze)
    logger.info("Silver layer completed.")

    logger.info("Processing Gold layer...")
    df_gold = gold_customers(df_silver)
    logger.info("Gold layer completed.")

    logger.info("Pipeline completed!")
    return df_gold
