"""
Module to load CSS files
"""

import os
from typing import Union, List

import streamlit as st

def load_css(css_files: Union[str, List[str]] = None):
    """
    Function to load CSS files dynamically.
    
    Args:
        css_files (Union[str, List[str]], optional): Single CSS filename or list of CSS filenames.
            If None, loads all CSS files in the assets directory.
    """
    assets_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'customer_management/streamlit/assets'
    )
    
    if isinstance(css_files, str):
        css_files = [css_files]
    elif css_files is None:
        css_files = [f for f in os.listdir(assets_dir) if f.endswith('.css')]

    combined_css = ""
    
    for css_file in css_files:
        if not css_file.endswith('.css'):
            css_file += '.css'
            
        file_path = os.path.join(assets_dir, css_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                combined_css += f.read() + "\n"
        except FileNotFoundError:
            st.warning(f"CSS file not found: {css_file}")
            continue
    
    if combined_css:
        st.markdown(f'<style>{combined_css}</style>', unsafe_allow_html=True)
