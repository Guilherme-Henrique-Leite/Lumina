"""
Module to normalize country names.
"""
import pycountry
import pandas as pd

from customer_management.utils.country_mapping import COUNTRY_MAPPING, VALID_COUNTRIES

def normalize_country_name(country):
    """
    Normalize the country name using official mappings.
    
    Args:
        country (str): Country name to be normalized
        
    Returns:
        str: Normalized country name or None if invalid
    """
    if pd.isna(country) or country.strip() == '':
        return None
        
    country = country.strip().replace('!@#', '').replace('unknown', '')
    
    if country in COUNTRY_MAPPING:
        return COUNTRY_MAPPING[country]
        
    if country in VALID_COUNTRIES:
        return VALID_COUNTRIES[country]
        
    try:
        result = pycountry.countries.search_fuzzy(country)
        if result:
            return VALID_COUNTRIES.get(result[0].name)
    except:
        pass
        
    return None