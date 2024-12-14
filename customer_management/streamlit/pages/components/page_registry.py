"""
Module to register pages
"""

from customer_management.streamlit.pages import (
    customer_panel,
    overview,
    customer_registration
)


def get_pages():
    """
    Get pages dictionary with lazy imports to avoid circular dependencies
    """
    from customer_management.streamlit.pages import (
        graphic_visualization
    )
    
    return {
        "Visão Geral": overview.run,
        "Painel de Clientes": customer_panel.run,
        "Visualização Gráfica": graphic_visualization.run,
        "Cadastro de Clientes": customer_registration.run,
    }
