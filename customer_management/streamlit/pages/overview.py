"""
Module for metrics overview visualization
"""
import streamlit as st
import time

from customer_management.utils import load_css
from customer_management.utils import run_data_pipeline

from customer_management.streamlit.visualizations import (
    render_progress_section,
    render_metric_cards,
    render_statistics,
    create_trend_chart
)

def run():
    """Run the metrics overview page"""
    load_css('metrics.css')
    
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
        time.sleep(0.5)
        success_placeholder.empty()
    
    df = st.session_state['df_gold']
    meta_clientes = 10000
    
    render_progress_section(df, meta_clientes)
    st.markdown("<br>", unsafe_allow_html=True)
    render_metric_cards(df, meta_clientes)
    st.plotly_chart(create_trend_chart(df), use_container_width=True)
    
    with st.expander('📊 Detalhamento por Bairro', expanded=True):
        col_table, col_stats = st.columns([3, 1])
        
        with col_table:
            st.markdown("### Análise de Distribuição")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                    <div style='background-color: rgba(0,0,0,0.2); padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
                        <h4 style='color: gray; margin: 0;'>Concentração de Mercado</h4>
                        <p style='color: white; font-size: 14px; margin: 10px 0;'>
                            Os dois principais bairros concentram 
                            <span style='color: #32CD32; font-weight: bold;'>
                                {:.1f}%
                            </span> 
                            dos clientes
                        </p>
                    </div>
                """.format(df['Bairro'].value_counts().iloc[0:2].sum() / len(df) * 100), unsafe_allow_html=True)
                
            with col2:
                st.markdown("""
                    <div style='background-color: rgba(0,0,0,0.2); padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
                        <h4 style='color: gray; margin: 0;'>Potencial de Crescimento</h4>
                        <p style='color: white; font-size: 14px; margin: 10px 0;'>
                            Os três bairros menos atendidos representam apenas 
                            <span style='color: #32CD32; font-weight: bold;'>
                                {:.1f}%
                            </span> 
                            do mercado
                        </p>
                    </div>
                """.format(df['Bairro'].value_counts().iloc[-3:].sum() / len(df) * 100), unsafe_allow_html=True)
            
            neighborhood_data = df['Bairro'].value_counts().reset_index()
            neighborhood_data.columns = ['Bairro', 'Clientes']
            neighborhood_data['Percentual'] = (neighborhood_data['Clientes'] / len(df) * 100).round(1)
            
            col_search, col_filter = st.columns([2, 1])
            
            with col_search:
                bairros = ["Todos"] + neighborhood_data['Bairro'].tolist()
                selected_bairro = st.selectbox(
                    "🔍 Selecione o bairro",
                    bairros,
                    index=0
                )
            
            with col_filter:
                sort_by = st.selectbox(
                    "Ordenar por",
                    ["Clientes (Maior)", "Clientes (Menor)", "Alfabético"],
                    index=0
                )
            
            if selected_bairro != "Todos":
                neighborhood_data = neighborhood_data[
                    neighborhood_data['Bairro'] == selected_bairro
                ]

            if sort_by == "Clientes (Maior)":
                neighborhood_data = neighborhood_data.sort_values('Clientes', ascending=False)
            elif sort_by == "Clientes (Menor)":
                neighborhood_data = neighborhood_data.sort_values('Clientes', ascending=True)
            else:
                neighborhood_data = neighborhood_data.sort_values('Bairro')
            
            st.markdown(f"**{len(neighborhood_data)}** bairros encontrados")
            
            st.dataframe(
                neighborhood_data,
                column_config={
                    "Bairro": st.column_config.TextColumn(
                        "Bairro",
                        help="Nome do bairro"
                    ),
                    "Clientes": st.column_config.NumberColumn(
                        "Clientes",
                        help="Número total de clientes",
                        format="%d"
                    ),
                    "Percentual": st.column_config.NumberColumn(
                        "Percentual",
                        help="Percentual do total de clientes",
                        format="%.1f%%"
                    ),
                },
                hide_index=True,
                use_container_width=True,
                height=350
            )
            
        with col_stats:
            render_statistics(df)