"""
Module for neighborhood analysis components
"""
import streamlit as st
import plotly.graph_objects as go

def render_neighborhood_analysis(df):
    """Render the complete neighborhood analysis section"""
    col_table, col_stats = st.columns([3, 1])
    
    with col_table:
        st.markdown("### Análise de Distribuição")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div style='background-color: rgba(0,0,0,0.2); padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
                    <h4 style='color: gray; margin: 0;'>Concentração de Mercado</h4>
                    <p style='color: white; font-size: 14px; margin: 10px 0;'>
                        Os dois principais bairros concentram 
                        <span style='color: #32CD32; font-weight: bold;'>
                            {:.1f}%
                        </span> 
                        dos clientes
                    </p>
                </div>
            """.format(df['Bairro'].value_counts().iloc[0:2].sum() / len(df) * 100), unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
                <div style='background-color: rgba(0,0,0,0.2); padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
                    <h4 style='color: gray; margin: 0;'>Potencial de Crescimento</h4>
                    <p style='color: white; font-size: 14px; margin: 10px 0;'>
                        Os três bairros menos atendidos representam apenas 
                        <span style='color: #32CD32; font-weight: bold;'>
                            {:.1f}%
                        </span> 
                        do mercado
                    </p>
                </div>
            """.format(df['Bairro'].value_counts().iloc[-3:].sum() / len(df) * 100), unsafe_allow_html=True)
        
        neighborhood_data = df['Bairro'].value_counts().reset_index()
        neighborhood_data.columns = ['Bairro', 'Clientes']
        neighborhood_data['Percentual'] = (neighborhood_data['Clientes'] / len(df) * 100).round(1)
        
        col_search, col_filter = st.columns([2, 1])
        
        with col_search:
            bairros = ["Todos"] + neighborhood_data['Bairro'].tolist()
            selected_bairro = st.selectbox(
                "🔍 Selecione o bairro",
                bairros,
                index=0
            )
        
        with col_filter:
            sort_by = st.selectbox(
                "Ordenar por",
                ["Clientes (Maior)", "Clientes (Menor)", "Alfabético"],
                index=0
            )
        
        if selected_bairro != "Todos":
            neighborhood_data = neighborhood_data[
                neighborhood_data['Bairro'] == selected_bairro
            ]
        
        if sort_by == "Clientes (Maior)":
            neighborhood_data = neighborhood_data.sort_values('Clientes', ascending=False)
        elif sort_by == "Clientes (Menor)":
            neighborhood_data = neighborhood_data.sort_values('Clientes', ascending=True)
        else:
            neighborhood_data = neighborhood_data.sort_values('Bairro')
        
        st.markdown(f"**{len(neighborhood_data)}** bairros encontrados")
        
        st.dataframe(
            neighborhood_data,
            column_config={
                "Bairro": st.column_config.TextColumn(
                    "Bairro",
                    help="Nome do bairro"
                ),
                "Clientes": st.column_config.NumberColumn(
                    "Clientes",
                    help="Número total de clientes",
                    format="%d"
                ),
                "Percentual": st.column_config.NumberColumn(
                    "Percentual",
                    help="Percentual do total de clientes",
                    format="%.1f%%"
                ),
            },
            hide_index=True,
            use_container_width=True,
            height=350
        )
    
    with col_stats:
        render_statistics(df)

def render_statistics(df):
    """Render statistics section"""
    st.markdown("""
        <style>
            .stat-box {
                background-color: rgba(0, 0, 0, 0.2);
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 15px;
            }
            .stat-label {
                color: #808080;
                font-size: 13px;
                margin-bottom: 8px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            .stat-value {
                color: white;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 5px;
            }
            .stat-highlight {
                color: #32CD32;
                font-size: 24px;
            }
            .stat-subvalue {
                color: #808080;
                font-size: 13px;
                opacity: 0.8;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; color: white;'>Estatísticas</h3>", unsafe_allow_html=True)
    
    total_bairros = df['Bairro'].nunique()
    media_por_bairro = len(df) / total_bairros
    bairro_mais_populoso = df['Bairro'].value_counts().iloc[0]
    bairro_menos_populoso = df['Bairro'].value_counts().iloc[-1]
    
    stats = [
        {
            "label": "Total de Bairros Atendidos",
            "value": f"{total_bairros}",
            "highlight": False
        },
        {
            "label": "Média de Clientes por Bairro",
            "value": f"{media_por_bairro:.1f}",
            "highlight": False
        },
        {
            "label": "Maior Potencial de Negócios",
            "value": df['Bairro'].value_counts().index[0],
            "subvalue": f"Concentração de {(bairro_mais_populoso/len(df)*100):.1f}% dos clientes",
            "highlight": True
        },
        {
            "label": "Oportunidade de Expansão",
            "value": df['Bairro'].value_counts().index[-1],
            "subvalue": f"Apenas {(bairro_menos_populoso/len(df)*100):.1f}% de presença",
            "highlight": True
        }
    ]
    
    for stat in stats:
        value_class = "stat-value stat-highlight" if stat.get("highlight") else "stat-value"
        html = f"""
            <div class="stat-box">
                <div class="stat-label">{stat['label']}</div>
                <div class="{value_class}">{stat['value']}</div>
                {f'<div class="stat-subvalue">{stat["subvalue"]}</div>' if "subvalue" in stat else ""}
            </div>
        """
        st.markdown(html, unsafe_allow_html=True)