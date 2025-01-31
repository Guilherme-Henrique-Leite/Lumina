"""
Module to outsource Streamlit pages
"""

import streamlit as st
from streamlit_option_menu import option_menu

from .overview import run as overview
from .customer_registration import run as customer_registration
from .customer_panel import run as customer_panel
from .graphic_visualization import run as graphic_visualization

from customer_management.streamlit.pages.components.sidebar import render_sidebar
from customer_management.streamlit.pages.components.grid_config import render_grid

PAGE_CONFIG = {
    "Visão Geral": overview,
    "Cadastro de Clientes": customer_registration,
    "Painel de Clientes": customer_panel,
    "Visualização Gráfica": graphic_visualization
}

def get_pages():
    return PAGE_CONFIG

def render_sidebar():
    """
    Renders the sidebar menu for navigation.

    Return:
        page (str): The selected page from the sidebar menu.
    """
    with st.sidebar:
        st.title("Menu de Navegação")
        page = option_menu(
            menu_title=None,
            options=["Visão Geral", "Painel de Clientes", "Visualização Gráfica", "Cadastro de Clientes"],
            icons=["house", "clipboard-data", "bar-chart-fill", "person-circle"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#262730"},
                "icon": {"color": "lightgreen", "font-size": "20px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                "nav-link-selected": {"background-color": "#009603"},
            },
        )
    return page