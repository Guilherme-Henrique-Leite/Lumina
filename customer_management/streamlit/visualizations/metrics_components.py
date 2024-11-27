"""
Module for metrics visualization components
"""
import streamlit as st
from datetime import datetime, timedelta
import plotly.graph_objects as go

def create_progress_indicator(value, max_value):
    """Create a circular progress indicator"""
    percentage = min((value / max_value) * 100, 100)
    
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=percentage,
        domain={'x': [0.1, 0.9], 'y': [0.15, 0.85]},
        gauge={
            'axis': {'range': [0, 100], 'visible': False},
            'bar': {'color': "rgb(50, 205, 50)"},
            'bgcolor': "rgba(30, 30, 30, 0.7)",
            'borderwidth': 0,
            'shape': "angular",
        },
        number={
            'font': {'color': "white", 'size': 40, 'family': "Arial Black"},
            'suffix': "%"
        },
        title={
            'text': f"{value:,} / {max_value:,}",
            'font': {'color': "gray", 'size': 14, 'family': "Arial"},
            'align': 'center'
        }
    ))
    
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=250,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    
    return fig

def create_metric_card(title, value):
    """Create a metric card with consistent styling"""
    return f"""
        <div class="metric-container">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value:,}</div>
        </div>
    """

def render_progress_section(df, meta_clientes):
    """Render the progress indicator section"""
    col_left, col_center, col_right = st.columns([1, 2, 1])
    
    with col_center:
        progress_fig = create_progress_indicator(len(df), meta_clientes)
        st.plotly_chart(progress_fig, use_container_width=True)
        st.markdown('<div style="text-align: center; color: gray; margin-top: -20px;">Progresso</div>', 
                   unsafe_allow_html=True)

def render_metric_cards(df, meta_clientes):
    """Render the metric cards section"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(create_metric_card("Total de Clientes", len(df)), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card("Meta de Clientes", meta_clientes), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card("Cidades Atendidas", df['Cidade'].nunique()), unsafe_allow_html=True)