"""
Module to transform data from the silver layer to the gold layer.
"""
import logging

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
    initial_records = len(df_silver)
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
    
    final_records = len(df_gold)
    removed_records = initial_records - final_records
    
    logger.info(f"""
    Ready:
    - Initial records: {initial_records}
    - Valid records: {final_records}
    - Removed records: {removed_records} ({(removed_records/initial_records)*100:.1f}%)
    """)
    
    return df_gold
