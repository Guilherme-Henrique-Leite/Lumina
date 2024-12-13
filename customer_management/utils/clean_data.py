"""
Module to clean and validate data from the silver layer.
"""
from customer_management.utils import clean_contact
from customer_management.utils import is_valid_email

def clean_and_validate_data(df):
    """
    Cleans and validates a DataFrame of customer data.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The cleaned and validated DataFrame.
    """
    df = df.dropna(subset=['name'])
    df['contact'] = df['contact'].fillna('No Contact Info')
    df['email'] = df['email'].fillna('unknown@domain.com')
    df['country'] = df['country'].fillna('unknown country')
    df['city'] = df['city'].fillna('unknown city')
    df['neighborhood'] = df['neighborhood'].fillna('unknown neighborhood')
    df = df[df['email'].apply(is_valid_email)]  
    df['contact'] = df['contact'].apply(clean_contact)
    return df
