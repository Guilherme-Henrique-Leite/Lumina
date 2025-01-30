"""
Module to run Streamlit Page
"""
import streamlit as st


from customer_management.streamlit.pages import render_sidebar
from customer_management.streamlit.pages import get_pages

st.set_page_config(
    page_title="Lumina",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="☀️"
)

page = render_sidebar()
pages = get_pages()
pages[page]()
