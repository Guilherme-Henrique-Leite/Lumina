"""
Module to map countries to their Portuguese names.
"""
import pycountry

COUNTRY_MAPPING = {
    'United Kingdom': 'Reino Unido',
    'Germany': 'Alemanha',
    'Norway': 'Noruega',
    'Romania': 'Romênia',
    'Poland': 'Polônia',
    'Italy': 'Itália',
    'Malta': 'Malta',
    'Armenia': 'Armênia',
    
    'United States': 'Estados Unidos',
    'USA': 'Estados Unidos',
    'US': 'Estados Unidos',
    'Brazil': 'Brasil',
    'Ecuador': 'Equador',
    'Guatemala': 'Guatemala',
    
    'Japan': 'Japão',
    'Vanuatu': 'Vanuatu',
    
    'Saint Kitts and Nevis': 'São Cristóvão e Nevis'
}

VALID_COUNTRIES = {country.name: country.name for country in pycountry.countries}
VALID_COUNTRIES.update({
    'Taiwan': 'Taiwan',
    'Kosovo': 'Kosovo'
})