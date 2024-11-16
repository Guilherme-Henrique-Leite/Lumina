"""
Module to extract data
"""

import pandas as pd

from customer_management.utils import get_costumers

def bronze_customers(customers):
    df_customers = pd.DataFrame(get_costumers())
    customers = df_customers
    
    return customers

bronze_customers(customers=bronze_customers)
