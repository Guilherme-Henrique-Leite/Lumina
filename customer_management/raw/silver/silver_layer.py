import pandas as pd

from customer_management.raw import bronze_customers


def transform_bronze_layer():
    df_bronze = bronze_customers()
    print(df_bronze.shape)
    print()
    print(df_bronze.info())
    print()
    print(df_bronze.columns)
    
    object_columns = df_bronze.select_dtypes(include=['object']).columns
    print()
    print('object columns >>>', object_columns)
    
    columns_str = ['name', 'email', 'country']
    
    # df_bronze['country'] = df_bronze['country'].unique()
    
    print('TESTE DE MEMÓRIA COUNTRY (ANTES)')
    print('Número de valores únicos:', df_bronze['name'].nunique())
    print('Número total de linhas:', len(df_bronze))
    print('Uso de memória antes:', df_bronze['name'].memory_usage(deep=True))

    print()
    print('\nInformações do DataFrame antes da conversão:')
    print(df_bronze.info())

    print('\n<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>\n')

    print()
    print('APÓS CONVERSÃO PARA CATEGORY\n')
    df_bronze['name'] = df_bronze['name'].astype('category')

    print()
    print('Uso de memória após:', df_bronze['name'].memory_usage(deep=True))

    print()
    print('\nInformações do DataFrame após a conversão:')
    print(df_bronze.info())

    print()
    print('\nPrimeiros registros da coluna "country":')
    print(df_bronze['name'].head())
    
    
    # remove = lambda x: x.str.replace(',', '.').astype('float')
    
    # columns = ['name', 'email', 'contact', 'country']
    # for column in columns:
    #     df_bronze[column] = df_bronze[column].apply(remove)
    # print()
    # print('post for>>>>')
    # print(df_bronze.shape)
    
transform_bronze_layer()
    


def silver_customers():
    """
    Transform data from bronze layer and return it as a Dataframe
    """


silver_customers()