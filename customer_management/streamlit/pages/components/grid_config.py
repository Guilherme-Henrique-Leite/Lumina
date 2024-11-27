"""
Grid configuration module for data display settings.
"""
from typing import Dict, Any
from st_aggrid import AgGrid, GridOptionsBuilder


def configure_grid(df_filtered):
    """
    Configure grid with all original settings.
    """
    gb = GridOptionsBuilder.from_dataframe(df_filtered)
    gb.configure_pagination(
        paginationAutoPageSize=False, 
        paginationPageSize=20
    )
    
    gb.configure_selection(selection_mode='multiple', use_checkbox=True)
    gb.configure_grid_options(suppressRowClickSelection=True)
    gb.configure_grid_options(rowStyle={'background-color': '#ffffff'})
    gb.configure_grid_options(rowHoverClass='custom-hover')
    gb.configure_grid_options(
        rowClass='custom-row',
        rowSelection='multiple',
        suppressRowClickSelection=True,
        suppressCellSelection=True,
        accentedSort=True,
        rowStyle={'cursor': 'pointer'},
        selectedRowStyle={'background-color': 'rgba(35, 2, 77, 0.9)'},
        rowHoverStyle={'background-color': 'rgba(35, 2, 77, 0.9)'}
    )
    
    for column in ['Código Cliente', 'Nome', 'País', 'Cidade', 'Bairro']:
        gb.configure_column(column, 
                        filter=False,
                        menuTabs=['generalMenuTab'],
                        suppressMenu=True)
    
    gb.configure_default_column(editable=False, filter=False, sortable=True)
    gb.configure_grid_options(forceFitColumns=True)
    gb.configure_grid_options(
        localeText={
            'contains': 'Contém',
            'notContains': 'Não contém',
            'equals': 'Igual',
            'notEqual': 'Diferente',
            'startsWith': 'Começa com',
            'endsWith': 'Termina com',
            'filterOoo': 'Filtrar...',
            'noRowsToShow': 'Nenhum registro encontrado',
            'page': 'Página',
            'of': 'de',
            'to': 'até',
            'rows': 'linhas',
            'loadingOoo': 'Carregando...',
            'searchOoo': 'Buscar...',
            'selectAll': 'Selecionar Todos',
            'searchNullLabel': 'Vazio',
            'selectAllSearchResults': 'Selecionar Todos os Resultados',
            'clear': 'Limpar',
            'clearFilter': 'Limpar Filtro',
            'clearSearch': 'Limpar Busca',
            'contains_filterMenuTab': 'Filtro',
            'generalMenuTab': 'Geral',
            'pinColumn': 'Fixar Coluna',
            'autosizeThisColumn': 'Ajustar Esta Coluna',
            'autosizeAllColumns': 'Ajustar Todas as Colunas',
            'resetColumns': 'Redefinir Colunas',
            'pinLeft': 'Fixar à Esquerda',
            'pinRight': 'Fixar à Direita',
            'noPin': 'Não Fixar',
            'columns': 'Colunas',
            'pageSize': 'Tamanho da página',
            'Page Size': 'Tamanho da página',
            'rowsPerPage': 'Linhas por página',
            'loading': 'Carregando...',
            'first': 'Primeira',
            'previous': 'Anterior',
            'next': 'Próximo',
            'last': 'Última',
            'records': 'Registros',
            'items per page': 'itens por página',
            'selected': 'selecionado',
            'filtered': 'filtrado',
            'show': 'Mostrar',
            'items': 'itens',
            'all': 'Todos'
        }
    )
    
    return gb.build()


def render_grid(df_filtered):
    """
    Render grid with all original settings.
    """
    grid_options = configure_grid(df_filtered)
    
    return AgGrid(
        df_filtered,
        gridOptions=grid_options,
        height=600,
        width="100%",
        theme="streamlit",
        fit_columns_on_grid_load=True,
        domLayout="autoHeight",
        allow_unsafe_jscode=True,
        custom_css={
            ".ag-row-hover": {"background-color": "rgba(35, 2, 77, 0.9) !important"},
            ".ag-header-cell-label": {"justify-content": "center"},
            ".ag-row-selected": {"background-color": "rgba(35, 2, 77, 0.9) !important"},
            ".ag-checkbox-checked": {"color": "#32CD32 !important"},
            ".ag-checkbox-indeterminate": {"color": "#32CD32 !important"},
            ".ag-checkbox-input-wrapper::after": {"color": "#32CD32 !important"},
            ".ag-checkbox.ag-checked:after": {"color": "#32CD32 !important"},
            ".ag-checkbox.ag-checked > .ag-checkbox-input-wrapper": {"color": "#32CD32 !important"},
            ".ag-theme-streamlit .ag-checkbox-input-wrapper.ag-checked::after": {"color": "#32CD32 !important"},
            ".ag-cell-focus": {"border-color": "rgba(35, 2, 77, 0.9) !important"},
            ".ag-cell-range-selected": {"background-color": "rgba(35, 2, 77, 0.9) !important"},
            ".ag-cell-range-selected-1": {"background-color": "rgba(35, 2, 77, 0.9) !important"}
        }
    )