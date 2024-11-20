"""
Module to clean and validate contact information.
"""
import re


def clean_contact(contact):
    """
    Validates and cleans a contact string.

    Args:
        contact(str): The contact string to validate.

    Returns:
        str: The contact if valid, or 'Invalid Contact' otherwise.
    """
    
    if re.match(r'^[\d\-\+\(\)\s]+$', str(contact)):
        return contact
    else:
        return 'Invalid Contact'
