"""
Module to transform data from the silver layer to the gold layer.
"""
import pandas as pd
import logging

from customer_management.utils.country_mapping import COUNTRY_MAPPING, VALID_COUNTRIES
from customer_management.utils.normalize_country_names import normalize_country_name

logger = logging.getLogger(__name__)


def gold_customers(df_silver):
    """
    Transforms data from the Silver layer to the Gold layer.
    
    Args:
        df_silver (pd.DataFrame): Data from the Silver layer.
        
    Returns:
        pd.DataFrame: Processed data with standardized country names, 
                     cleaned locations and proper formatting.
    """
    registros_iniciais = len(df_silver)
    df_gold = df_silver.copy()
    
    df_gold.rename(
        columns={
            'id': 'Código Cliente',
            'name': 'Nome',
            'email': 'Email',
            'email_domain': 'Domínio',
            'contact': 'Contato',
            'country': 'País',
            'city': 'Cidade',
            'neighborhood': 'Bairro',
        },
        inplace=True,
    )
    
    df_gold['País'] = df_gold['País'].apply(normalize_country_name)
    
    df_gold = df_gold.dropna(subset=['País', 'Cidade', 'Bairro'])
    
    df_gold = df_gold[
        (df_gold['Cidade'] != 'NULL') & (df_gold['Cidade'].str.strip() != '') &
        (df_gold['Bairro'] != 'NULL') & (df_gold['Bairro'].str.strip() != '')
    ]
    
    df_gold['País'] = df_gold['País'].str.title()
    df_gold['Cidade'] = df_gold['Cidade'].str.title()
    df_gold['Bairro'] = df_gold['Bairro'].str.title()
    
    df_gold['Data_Processamento'] = pd.Timestamp.now()
    df_gold['Versao_Processamento'] = '1.0'
    
    registros_finais = len(df_gold)
    registros_removidos = registros_iniciais - registros_finais
    
    logger.info(f"""
    Processamento concluído:
    - Registros iniciais: {registros_iniciais}
    - Registros válidos: {registros_finais}
    - Registros removidos: {registros_removidos} ({(registros_removidos/registros_iniciais)*100:.1f}%)
    """)
    
    return df_gold
