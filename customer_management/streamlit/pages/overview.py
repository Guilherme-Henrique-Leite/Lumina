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
    
    placeholder = st.empty()
    if 'df_gold' not in st.session_state:
        with placeholder.container():
            st.info("Carregando dados automaticamente... Aguarde alguns segundos.")
        df_gold = run_data_pipeline()
        st.session_state['df_gold'] = df_gold
        placeholder.empty()
        success_placeholder = st.empty()
        with success_placeholder.container():
            st.success("Dados carregados com sucesso!")
        time.sleep(3)
        success_placeholder.empty()

    df = st.session_state['df_gold']
    df_filtered = df.copy()

    st.header("Dados Gerais")
    if df_filtered.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
    else:
        with st.expander("Filtros", expanded=False):
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                filter_client_code = st.multiselect(
                    "Código Cliente:",
                    options=df['Código Cliente'].unique(),
                    default=[],
                )
                
            with col2:
                filter_name = st.multiselect(
                    "Nome:",
                    options=df['Nome'].unique(),
                    default=[],
                )
            
            with col3:
                filter_country = st.multiselect(
                    "País:",
                    options=df['País'].unique(),
                    default=[],
                )
            with col4:
                filter_city = st.multiselect(
                    "Cidade:",
                    options=df['Cidade'].unique(),
                    default=[],
                )
            with col5:
                filter_neighborhood = st.multiselect(
                    "Bairro:",
                    options=df['Bairro'].unique(),
                    default=[],
                )
            
            

        if filter_client_code:
            df_filtered = df_filtered[df_filtered['Código Cliente'].isin(filter_client_code)]
        elif filter_name:
            df_filtered = df_filtered[df_filtered['Nome'].isin(filter_name)]    
        elif filter_country:
            df_filtered = df_filtered[df_filtered['País'].isin(filter_country)]
        elif filter_city:
            df_filtered = df_filtered[df_filtered['Cidade'].isin(filter_city)]
        elif filter_neighborhood:
            df_filtered = df_filtered[df_filtered['Bairro'].isin(filter_neighborhood)]
        
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