"""
Module to define model customers
"""
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from customer_management.utils import table_registry

@table_registry.mapped_as_dataclass
class Customer:
    """
    Class to mapped columns of table customers
    """

    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    contact: Mapped[str]
    country: Mapped[str]
