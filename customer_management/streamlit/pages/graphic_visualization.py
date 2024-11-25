"""
Module to display graphical visualizations
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def run():
    st.title("Visualização Gráfica")

    if 'df_gold' not in st.session_state:
        st.warning("Nenhum dado encontrado. Por favor, carregue os dados na página 'Visão Geral'.")
        return

    df = st.session_state['df_gold']

    st.header("Distribuição de Clientes por País")
    df_paises = df['País'].value_counts().reset_index()
    df_paises.columns = ['País', 'Quantidade']

    fig1 = go.Figure(
        data=[
            go.Bar(
                x=df_paises['País'],
                y=df_paises['Quantidade'],
                marker=dict(color="lightgreen"),
            )
        ]
    )
    fig1.update_layout(
        title="Distribuição de Clientes por País",
        xaxis_title="País",
        yaxis_title="Número de Clientes",
        template="plotly_dark",
        xaxis=dict(tickangle=45),
        height=600,
        margin=dict(l=20, r=20, t=50, b=50),
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.header("Distribuição Percentual por País")
    fig2 = px.pie(
        df_paises,
        names='País',
        values='Quantidade',
        title="Distribuição Percentual de Clientes por País",
        template="plotly_dark",
    )
    fig2.update_traces(textinfo='percent+label')
    st.plotly_chart(fig2, use_container_width=True)
