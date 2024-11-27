from typing import DataFrame

def validate_dataframe(df: DataFrame) -> bool:
    required_columns = ['País', 'Cidade', 'Bairro', 'Código Cliente', 'Nome']
    return all(column in df.columns for column in required_columns)