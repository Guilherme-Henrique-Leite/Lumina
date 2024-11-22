"""
Module to convert data to an Excel
"""

import pandas as pd

from io import BytesIO

def convert_df_to_excel(df):
    """
    Convert a DataFrame to an Excel file in memory.
    
    Args:
        df (pd.DataFrame): DataFrame to convert.

    Returns:
        BytesIO: Binary Excel file in memory.
    """
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Gold Layer')
    output.seek(0)
    
    return output