"""
Module to display all data
"""
import time

import streamlit as st

from customer_management.utils import load_css
from customer_management.utils import run_data_pipeline
from customer_management.utils import convert_df_to_excel

from customer_management.streamlit.pages.components.grid_config import render_grid


def run():
    """
    Function to run overview in display
    """
    load_css()
    st.title("Painel de Clientes")
    
    if 'df_gold' not in st.session_state:
        st.warning("Nenhum dado encontrado. Por favor, retorne à página principal.")
        return
    
    df = st.session_state['df_gold']
    
    if 'filter_client_code' not in st.session_state:
        st.session_state.filter_client_code = []
    if 'filter_name' not in st.session_state:
        st.session_state.filter_name = []
    if 'filter_country' not in st.session_state:
        st.session_state.filter_country = []
    if 'filter_city' not in st.session_state:
        st.session_state.filter_city = []
    if 'filter_neighborhood' not in st.session_state:
        st.session_state.filter_neighborhood = []
    
    def clear_filters():
        st.session_state.filter_client_code = []
        st.session_state.filter_name = []
        st.session_state.filter_country = []
        st.session_state.filter_city = []
        st.session_state.filter_neighborhood = []
    
    def clean_session_state(field, available_options):
        st.session_state[field] = [
            x for x in st.session_state[field] 
            if x in available_options
        ]

    df_filtered = df.copy()

    st.header("Dados Gerais")
    if df_filtered.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
    else:
        with st.expander("Filtros", expanded=False):
            df_filtered = df.copy()
            
            if st.session_state.filter_city:
                df_filtered = df_filtered[df_filtered['Cidade'].isin(st.session_state.filter_city)]
            if st.session_state.filter_name:
                df_filtered = df_filtered[df_filtered['Nome'].isin(st.session_state.filter_name)]
            if st.session_state.filter_country:
                df_filtered = df_filtered[df_filtered['País'].isin(st.session_state.filter_country)]
            if st.session_state.filter_client_code:
                df_filtered = df_filtered[df_filtered['Código Cliente'].isin(st.session_state.filter_client_code)]
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                clean_session_state('filter_client_code', df_filtered['Código Cliente'].unique())
                filter_client_code = st.multiselect(
                    "Código Cliente:",
                    options=df_filtered['Código Cliente'].unique(),
                    key='filter_client_code'
                )
            
            with col2:
                clean_session_state('filter_name', df_filtered['Nome'].unique())
                filter_name = st.multiselect(
                    "Nome:",
                    options=df_filtered['Nome'].unique(),
                    key='filter_name'
                )
            
            with col3:
                clean_session_state('filter_country', df_filtered['País'].unique())
                filter_country = st.multiselect(
                    "País:",
                    options=df_filtered['País'].unique(),
                    key='filter_country'
                )
            
            with col4:
                clean_session_state('filter_city', df_filtered['Cidade'].unique())
                filter_city = st.multiselect(
                    "Cidade:",
                    options=df_filtered['Cidade'].unique(),
                    key='filter_city'
                )
            
            with col5:
                clean_session_state('filter_neighborhood', df_filtered['Bairro'].unique())
                filter_neighborhood = st.multiselect(
                    "Bairro:",
                    options=df_filtered['Bairro'].unique(),
                    key='filter_neighborhood'
                )

            if filter_client_code:
                df_filtered = df_filtered[df_filtered['Código Cliente'].isin(filter_client_code)]
            if filter_name:
                df_filtered = df_filtered[df_filtered['Nome'].isin(filter_name)]
            if filter_country:
                df_filtered = df_filtered[df_filtered['País'].isin(filter_country)]
            if filter_city:
                df_filtered = df_filtered[df_filtered['Cidade'].isin(filter_city)]
            if filter_neighborhood:
                df_filtered = df_filtered[df_filtered['Bairro'].isin(filter_neighborhood)]
            
            st.button("Limpar Filtros", on_click=clear_filters)


        render_grid(df_filtered)

        col_download, _ = st.columns([1, 4])
        with col_download:
            excel_data = convert_df_to_excel(df_filtered)
            st.markdown(
                f'''
                <a href="#" class="download-button" download="dados_clientes.xlsx">
                    <i class="fas fa-download"></i> Baixar Excel
                </a>
                ''',
                unsafe_allow_html=True
            )