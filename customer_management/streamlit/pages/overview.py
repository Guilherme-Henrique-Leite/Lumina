"""
Module to display all data
"""
import time
import streamlit as st
from customer_management.utils import run_data_pipeline
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

def run():
    """
    Function to run overview in display
    """
    st.title("Visão Geral")

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

    st.subheader("Filtros")
    col1, col2 = st.columns([1, 1])
    with col1:
        filter_country = st.multiselect(
            "Filtrar por País:",
            options=df['País'].unique(),
            default=[],
        )
    with col2:
        filter_domain = st.multiselect(
            "Filtrar por Domínio:",
            options=df['Domínio'].unique(),
            default=[],
        )

    df_filtered = df.copy()
    if filter_country:
        df_filtered = df_filtered[df_filtered['País'].isin(filter_country)]
    if filter_domain:
        df_filtered = df_filtered[df_filtered['Domínio'].isin(filter_domain)]

    st.header("Métricas Principais")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Clientes", len(df_filtered))
    col2.metric("Países Atendidos", df_filtered['País'].nunique())
    col3.metric("Domínio Mais Comum", df_filtered['Domínio'].mode()[0] if not df_filtered.empty else "N/A")

    st.header("Dados Gerais")
    if df_filtered.empty:
        st.warning("Nenhum dado encontrado com os filtros selecionados.")
    else:
        gb = GridOptionsBuilder.from_dataframe(df_filtered)
        gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=20)
        gb.configure_default_column(editable=False, filter=True, sortable=True)
        gb.configure_grid_options(forceFitColumns=True)
        grid_options = gb.build()

        AgGrid(
            df_filtered,
            gridOptions=grid_options,
            height=600,
            width="100%",
            theme="streamlit",
            fit_columns_on_grid_load=True,
            domLayout="autoHeight",
        )
