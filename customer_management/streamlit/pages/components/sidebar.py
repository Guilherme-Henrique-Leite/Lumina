"""
Module to render the sidebar for the application
"""

import streamlit as st

from streamlit_option_menu import option_menu

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
