"""
Module to transform data from the silver layer to the gold layer.
"""

def gold_customers(df_silver):
    """
    Transforms data from the Silver layer to the Gold layer.

    Args:
        df_silver(pd.DataFrame): Data from the Silver layer.

    Returns:
        pd.DataFrame: Gold layer data ready for displayed.
    """
    
    df_silver.rename(
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
    
    df_gold = df_silver.dropna(subset=['País', 'Cidade', 'Bairro'])
    
    df_gold = df_gold[
        (df_gold['País'] != 'NULL') & (df_gold['País'].str.strip() != '') &
        (df_gold['Cidade'] != 'NULL') & (df_gold['Cidade'].str.strip() != '') &
        (df_gold['Bairro'] != 'NULL') & (df_gold['Bairro'].str.strip() != '')
    ]
    
    
    return df_gold
