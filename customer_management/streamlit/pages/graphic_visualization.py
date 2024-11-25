"""
Module to display graphical visualizations
"""
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

def run():
    """
    Function to run charts in display
    """
    
    st.title("Visualização Gráfica")

    if 'df_gold' not in st.session_state:
        st.warning("Nenhum dado encontrado. Por favor, carregue os dados na página 'Visão Geral'.")
        return

    df = st.session_state['df_gold']

    st.header("Distribuição de Clientes por País")
    df_country = df['País'].value_counts().reset_index()
    df_country.columns = ['País', 'Quantidade']

    bar_chart = go.Figure(
        data=[
            go.Bar(
                x=df_country['País'],
                y=df_country['Quantidade'],
                marker=dict(color="lightgreen"),
            )
        ]
    )
    bar_chart.update_layout(
        title="Distribuição de Clientes por País",
        xaxis_title="País",
        yaxis_title="Número de Clientes",
        template="plotly_dark",
        xaxis=dict(tickangle=45),
        height=600,
        margin=dict(l=20, r=20, t=50, b=50),
    )
    st.plotly_chart(bar_chart)

    st.header("Distribuição Percentual por País")
    pie_chart = px.pie(
        df_country,
        names='País',
        values='Quantidade',
        title="Distribuição Percentual de Clientes por País",
        template="plotly_dark",
    )
    pie_chart.update_traces(textinfo='percent+label')
    st.plotly_chart(pie_chart)
