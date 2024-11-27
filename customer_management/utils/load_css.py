"""
Module to load the CSS file
"""

import os

import streamlit as st

def load_css():
    """
    Function to load the CSS file.
    """
    css_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'customer_management/streamlit/assets',
        'styles.css'
    )
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
