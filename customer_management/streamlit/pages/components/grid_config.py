"""
Grid configuration module for data display settings.
"""
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


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


def render_grid(df):
    """
    Renders an AG Grid with the provided DataFrame
    """
    gb = GridOptionsBuilder.from_dataframe(df)
    
    gb.configure_default_column(
        resizable=True,
        filterable=False,
        sortable=True,
        editable=False,
        suppressSizeToFit=False,
        menuTabs=['generalMenuTab'],
        suppressMenu=True
    )
    
    column_configs = {
        "Código Cliente": {"flex": 0.7},
        "Nome": {"flex": 1.2},
        "Email": {"flex": 1.5},
        "Contato": {"flex": 1},
        "País": {"flex": 0.8},
        "Estado": {"flex": 0.8},
        "Cidade": {"flex": 1},
        "Bairro": {"flex": 1},
        "created_at": {"flex": 1, "header_name": "Data de Cadastro"},
        "Domínio": {"flex": 1}
    }
    
    for col, config in column_configs.items():
        header_name = config.get('header_name', col)
        gb.configure_column(
            col,
            header_name=header_name,
            filter=False,
            menuTabs=['generalMenuTab'],
            suppressMenu=True,
            flex=config['flex'],
            suppressSizeToFit=False,
            resizable=True
        )
    
    gb.configure_grid_options(
        domLayout='normal',
        rowHeight=40,
        headerHeight=45,
        enableRangeSelection=True,
        suppressRowClickSelection=True,
        pagination=True,
        paginationAutoPageSize=False,
        paginationPageSize=20,
        suppressMenuHide=True,
        suppressFilter=True,
        suppressColumnVirtualisation=True,
        suppressRowVirtualisation=True,
    )
    
    grid_options = gb.build()
    
    return AgGrid(
        df,
        gridOptions=grid_options,
        enable_enterprise_modules=False,
        allow_unsafe_jscode=False,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        height=800,
        fit_columns_on_grid_load=True,
        theme='streamlit',
        custom_css={
            "#gridToolBar": {"display": "none"},
            ".ag-root-wrapper": {
                "border": "1px solid rgba(255, 255, 255, 0.1)",
                "border-radius": "4px",
                "background-color": "transparent"
            },
            ".ag-header": {
                "background-color": "transparent"
            },
            ".ag-row": {
                "background-color": "transparent"
            },
            ".ag-row-even": {
                "background-color": "rgba(255, 255, 255, 0.02)"
            },
            ".ag-row-odd": {
                "background-color": "transparent"
            },
            ".ag-row-hover": {
                "background-color": "rgba(11, 74, 11, 0.95) !important"
            },
            ".ag-header-cell-menu-button": {
                "display": "none"
            }
        }
    )