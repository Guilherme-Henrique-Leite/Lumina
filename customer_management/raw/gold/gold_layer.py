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
        },
        inplace=True,
    )

    return df_silver
