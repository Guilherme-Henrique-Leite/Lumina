"""
Module to display all data
"""
import pandas as pd

import streamlit as st

from customer_management.utils import load_css
from customer_management.utils import run_data_pipeline
from customer_management.utils import convert_df_to_excel

from customer_management.streamlit.pages.components.grid_config import render_grid


def get_sorted_unique_values(df, column):
    """Get sorted unique values from dataframe column, handling None values"""
    values = df[column].unique()
    values = [x for x in values if pd.notna(x)]
    return sorted(values)

def run():
    """
    Function to run overview in display
    """

    load_css()
    st.title("Painel de Clientes")
    
    if 'full_dataframe' not in st.session_state:
        st.session_state['full_dataframe'] = run_data_pipeline()
    
    df = st.session_state['full_dataframe']
    
    def clear_filters():
        keys_to_clear = [
            'filter_client_code', 'filter_name', 'filter_country',
            'filter_state', 'filter_city', 'filter_neighborhood',
            'filter_date_start', 'filter_date_end'
        ]
        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
    
    st.header("Dados Gerais")
    
    df_filtered = st.session_state['full_dataframe'].copy()
    
    with st.expander("Filtros", expanded=False):
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            filter_client_code = st.multiselect(
                "Código Cliente:",
                options=get_sorted_unique_values(df, 'Código Cliente'),
                default=None,
                key='filter_client_code'
            )
            if filter_client_code:
                df_filtered = df_filtered[df_filtered['Código Cliente'].isin(filter_client_code)]
        
        with col2:
            filter_name = st.multiselect(
                "Nome:",
                options=get_sorted_unique_values(df_filtered, 'Nome'),
                default=None,
                key='filter_name'
            )
            if filter_name:
                df_filtered = df_filtered[df_filtered['Nome'].isin(filter_name)]
        
        with col3:
            filter_country = st.multiselect(
                "País:",
                options=get_sorted_unique_values(df_filtered, 'País'),
                default=None,
                key='filter_country'
            )
            if filter_country:
                df_filtered = df_filtered[df_filtered['País'].isin(filter_country)]
        
        with col4:
            filter_state = st.multiselect(
                "Estado:",
                options=get_sorted_unique_values(df_filtered, 'Estado'),
                default=None,
                key='filter_state'
            )
            if filter_state:
                df_filtered = df_filtered[df_filtered['Estado'].isin(filter_state)]
        
        with col5:
            filter_city = st.multiselect(
                "Cidade:",
                options=get_sorted_unique_values(df_filtered, 'Cidade'),
                default=None,
                key='filter_city'
            )
            if filter_city:
                df_filtered = df_filtered[df_filtered['Cidade'].isin(filter_city)]
        
        col6, col7, col8, col9, col10 = st.columns(5)
        
        with col6:
            filter_neighborhood = st.multiselect(
                "Bairro:",
                options=get_sorted_unique_values(df_filtered, 'Bairro'),
                default=None,
                key='filter_neighborhood'
            )
            if filter_neighborhood:
                df_filtered = df_filtered[df_filtered['Bairro'].isin(filter_neighborhood)]
        
        with col7, col8:
            df_filtered['created_at'] = pd.to_datetime(df_filtered['created_at'])
            
            min_date = df_filtered['created_at'].min().date()
            max_date = df_filtered['created_at'].max().date()
            
            date_col1, date_col2 = col7, col8
            with date_col1:
                start_date = st.date_input(
                    "Data Inicial:",
                    value=min_date,
                    min_value=min_date,
                    max_value=max_date,
                    key='filter_date_start',
                    format="DD/MM/YYYY"
                )
            
            with date_col2:
                end_date = st.date_input(
                    "Data Final:",
                    value=max_date,
                    min_value=min_date,
                    max_value=max_date,
                    key='filter_date_end',
                    format="DD/MM/YYYY"
                )
            
            if start_date and end_date:
                mask = (df_filtered['created_at'].dt.date >= start_date) & (df_filtered['created_at'].dt.date <= end_date)
                df_filtered = df_filtered[mask]
        
        if st.button("Limpar Filtros"):
            df_filtered = df.copy()
            clear_filters()
            st.rerun()

    if df_filtered.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
    else:
        render_grid(df_filtered)

        col_download, _ = st.columns([1, 4])
        with col_download:
            excel_data = convert_df_to_excel(df_filtered)
            st.download_button(
                label="📥 Baixar Excel",
                data=excel_data,
                file_name="dados_clientes.xlsx",
                mime="application/vnd.ms-excel"
            )