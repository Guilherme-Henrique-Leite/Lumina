"""
Module to run Streamlit Page
"""
import streamlit as st
import os
from pathlib import Path

from customer_management.streamlit.pages import overview
from customer_management.streamlit.pages import render_sidebar
from customer_management.streamlit.pages import graphic_visualization


st.set_page_config(
    page_title="Painel de Gerenciamento",
    layout="wide",
    initial_sidebar_state="auto",
)

page = render_sidebar()

if page == "Painel Geral":
    overview.run()
elif page == "Visualização Gráfica":
    graphic_visualization.run()
