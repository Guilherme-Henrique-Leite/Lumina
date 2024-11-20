"""
Module to validate email addresses.
"""
import re

def is_valid_email(email):
    """
    Checks if the given email address is valid.

    Uses a regex pattern to verify the format of the email address.
    
    Args:
        email(str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))
