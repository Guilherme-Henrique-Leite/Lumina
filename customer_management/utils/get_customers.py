"""
Module to get all customers
"""


from sqlalchemy import text

from customer_management.database import engine

def get_costumers():
    with engine.connect() as connection:
        result = connection.execute(text("select * from customers"))
    return result