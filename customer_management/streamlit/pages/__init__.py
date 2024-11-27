"""
Module to outsource Streamlit pages
"""

from customer_management.streamlit.pages import customer_panel
from customer_management.streamlit.pages import overview
from customer_management.streamlit.pages import graphic_visualization

from customer_management.streamlit.pages.components.sidebar import render_sidebar
from customer_management.streamlit.pages.components.grid_config import render_grid
from customer_management.streamlit.pages.components.page_registry import get_pages
