"""
Module to display all data
"""
import time
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

def get_session_id():
    """Generate a unique session ID for the current page view"""
    if 'last_page' not in st.session_state:
        st.session_state.last_page = 'panel'
    elif st.session_state.last_page != 'panel':
        if 'page_session_id' in st.session_state:
            del st.session_state.page_session_id
        st.session_state.last_page = 'panel'
    
    if 'page_session_id' not in st.session_state:
        st.session_state.page_session_id = str(int(time.time()))
    
    return st.session_state.page_session_id

@st.cache_data(ttl=None)
def run_cached_pipeline(session_id):
    """
    Cached version of data pipeline
    The session_id parameter ensures new cache when returning to page
    """
    return run_data_pipeline()

def apply_filters(df, filters):
    """Apply filters efficiently using query strings"""
    query_parts = []
    query_params = {}
    
    for column, values in filters.items():
        if values and len(values) > 0:
            param_name = f"filter_{column.lower().replace(' ', '_')}"
            query_parts.append(f"`{column}` in @{param_name}")
            query_params[param_name] = values
    
    if query_parts:
        return df.query(" and ".join(query_parts), local_dict=query_params)
    return df

def load_css():
    st.markdown("""
        <style>
        .stSpinner > div {
            text-align: center;
            font-size: 1.2rem;
            color: #4CAF50;
        }
        </style>
    """, unsafe_allow_html=True)

def run():
    """Function to run overview in display"""
    load_css()
    st.title("Painel de Clientes")
    
    session_id = get_session_id()
    
    with st.spinner('📊 Preparando visualização dos dados...'):
        df = run_cached_pipeline(session_id)
        
        st.header("Dados Gerais")
        df_filtered = df
        
        with st.expander("Filtros", expanded=False):
            filters = {}
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                filter_client_code = st.multiselect(
                    "Código Cliente:",
                    options=get_sorted_unique_values(df, 'Código Cliente'),
                    default=None,
                    key='filter_client_code'
                )
                if filter_client_code:
                    filters['Código Cliente'] = filter_client_code
            
            with col2:
                available_names = get_sorted_unique_values(
                    df_filtered if not filters else apply_filters(df, filters),
                    'Nome'
                )
                filter_name = st.multiselect(
                    "Nome:",
                    options=available_names,
                    default=None,
                    key='filter_name'
                )
                if filter_name:
                    filters['Nome'] = filter_name
            
            with col3:
                filter_country = st.multiselect(
                    "País:",
                    options=get_sorted_unique_values(df_filtered, 'País'),
                    default=None,
                    key='filter_country'
                )
                if filter_country:
                    filters['País'] = filter_country
            
            with col4:
                filter_state = st.multiselect(
                    "Estado:",
                    options=get_sorted_unique_values(df_filtered, 'Estado'),
                    default=None,
                    key='filter_state'
                )
                if filter_state:
                    filters['Estado'] = filter_state
            
            with col5:
                filter_city = st.multiselect(
                    "Cidade:",
                    options=get_sorted_unique_values(df_filtered, 'Cidade'),
                    default=None,
                    key='filter_city'
                )
                if filter_city:
                    filters['Cidade'] = filter_city
            
            col6, col7, col8, col9, col10 = st.columns(5)
            
            with col6:
                filter_neighborhood = st.multiselect(
                    "Bairro:",
                    options=get_sorted_unique_values(df_filtered, 'Bairro'),
                    default=None,
                    key='filter_neighborhood'
                )
                if filter_neighborhood:
                    filters['Bairro'] = filter_neighborhood
            
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
            
            if filters:
                df_filtered = apply_filters(df, filters)
            
            if 'filter_date_start' in st.session_state or 'filter_date_end' in st.session_state:
                date_mask = (
                    (df_filtered['created_at'].dt.date >= st.session_state.get('filter_date_start', df_filtered['created_at'].min().date())) &
                    (df_filtered['created_at'].dt.date <= st.session_state.get('filter_date_end', df_filtered['created_at'].max().date()))
                )
                df_filtered = df_filtered[date_mask]

            def has_active_filters():
                filter_keys = [
                    'filter_client_code', 'filter_name', 'filter_country',
                    'filter_state', 'filter_city', 'filter_neighborhood'
                ]
                has_multiselect_filters = any(
                    st.session_state.get(key, []) for key in filter_keys
                )
                
                default_start = df['created_at'].min().date()
                default_end = df['created_at'].max().date()
                has_date_filters = (
                    st.session_state.get('filter_date_start', default_start) != default_start or
                    st.session_state.get('filter_date_end', default_end) != default_end
                )
                
                return has_multiselect_filters or has_date_filters

            if st.button("Limpar Filtros"):
                if has_active_filters():
                    st.session_state.needs_reset = True
                    st.rerun()
                else:
                    st.info("Não há filtros ativos para limpar.")

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