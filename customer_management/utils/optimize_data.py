"""
Module to optimize memory usage in a DataFrame.
"""

def check_object(df, columns):
    """
    Identifies columns with dtype 'object'.

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list): Columns to check.

    Returns:
        list: Columns with dtype 'object'.
    """
    object_columns = []
    
    for col in columns:
        if df[col].dtype == 'object':
            object_columns.append(col)
    
    return object_columns


def optimize_memory(df, columns):
    """
    Converts columns to 'category' to reduce memory usage.

    Args:
        df (pd.DataFrame): The DataFrame to optimize.
        columns (list): Columns to analyze and convert.

    Returns:
        pd.DataFrame: Optimized DataFrame.
    """
    
    for col in columns:
        if df[col].nunique() / len(df) < 0.2:
            df[col] = df[col].astype('category')
        
    return df
