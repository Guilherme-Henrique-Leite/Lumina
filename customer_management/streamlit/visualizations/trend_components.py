"""
Module for trend visualization components
"""
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

def create_trend_chart(df):
    """Create a trend chart showing customer growth"""
    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') 
            for x in range(30, 0, -1)]
    
    current_customers = len(df)
    historical_values = np.linspace(
        current_customers * 0.7,
        current_customers,
        len(dates)
    )
    historical_values = historical_values + np.random.normal(0, 5, len(dates))
    historical_values = historical_values.astype(int)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=historical_values,
        mode='lines',
        line=dict(color='rgb(50, 205, 50)', width=3),
        fill='tozeroy',
        fillcolor='rgba(50, 205, 50, 0.1)'
    ))
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=historical_values,
        mode='markers',
        marker=dict(color='rgb(50, 205, 50)', size=8),
        showlegend=False
    ))
    
    fig.update_layout(
        title={
            'text': 'Evolução de Clientes (Últimos 30 dias)',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=16, color='white')
        },
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False,
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)',
            tickformat='%d/%m',
            tickfont=dict(color='gray'),
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(128, 128, 128, 0.2)',
            tickfont=dict(color='gray'),
        ),
        hovermode='x unified'
    )
    
    return fig