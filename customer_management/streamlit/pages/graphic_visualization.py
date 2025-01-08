"""
Module to display graphical visualizations
"""
import pytz
from datetime import datetime

import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go


def run():
    """
    Function to run charts in display
    """
    st.title("Visualização Gráfica")

    if 'df_gold' not in st.session_state:
        st.warning("Nenhum dado encontrado. Por favor, carregue os dados na página 'Visão Geral'.")
        return

    df = st.session_state['df_gold']

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Total de Clientes",
            f"{len(df):,}",
            help="Base total de clientes"
        )
    with col2:
        st.metric(
            "Países Atendidos",
            f"{df['País'].nunique()}",
            help="Alcance geográfico"
        )
    with col3:
        media_por_pais = len(df) / df['País'].nunique()
        st.metric(
            "Média por País",
            f"{media_por_pais:.0f}",
            help="Média de clientes por país"
        )

    tab1, tab2, tab3 = st.tabs([
        "Distribuição", 
        "Crescimento", 
        "Segmentação"
    ])

    with tab1:
        st.header("Distribuição de Clientes por País")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            df_country = df['País'].value_counts().reset_index()
            df_country.columns = ['País', 'Quantidade']
            
            df_country['Percentual'] = (df_country['Quantidade'] / df_country['Quantidade'].sum() * 100).round(1)
            
            fig = go.Figure()
 
            fig.add_trace(go.Bar(
                y=df_country.head(15)['País'],
                x=df_country.head(15)['Quantidade'],
                orientation='h',
                text=df_country.head(15)['Percentual'].apply(lambda x: f'{x}%'),
                textposition='auto',
                marker=dict(
                    color='#32CD32',
                    opacity=0.8,
                    line=dict(
                        color='#228B22',
                        width=1
                    )
                ),
                hovertemplate='País: %{y}<br>Clientes: %{x}<br>Percentual: %{text}<extra></extra>'
            ))
            
            fig.update_layout(
                title={
                    'text': 'Top 15 Países por Número de Clientes',
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'
                },
                xaxis_title='Número de Clientes',
                yaxis_title='País',
                template='plotly_dark',
                height=600,
                margin=dict(l=20, r=20, t=50, b=50),
                yaxis={'categoryorder':'total ascending'}
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### Análise de Mercado")
            
            total_paises = df['País'].nunique()
            total_clientes = len(df)
            media_por_pais = total_clientes / total_paises
            
            st.metric(
                "Total de Países",
                f"{total_paises}",
                help="Número de países com clientes"
            )
            
            st.metric(
                "Média por País",
                f"{media_por_pais:.0f}",
                help="Média de clientes por país"
            )
            
            st.markdown("### Mercados Principais")
            for i, row in df_country.head(3).iterrows():
                st.markdown(f"""
                **{row['País']}**
                - Volume: {row['Quantidade']} clientes
                - Participação: {row['Percentual']:.1f}%
                """)
                
            concentracao = df_country.head(5)['Quantidade'].sum() / total_clientes * 100
            st.markdown(f"""
            ### Análise de Concentração
            
            **Concentração de Mercado**
            - Top 5 países: {concentracao:.1f}% dos clientes
            - Índice de dispersão: {(100-concentracao):.1f}%
            
            **Indicadores de Mercado**
            - Distribuição geográfica
            - Participação por região
            - Ranking por volume
            """)

        st.divider()
        if st.button("Analisar Distribuição", type="primary"):
            st.subheader("Análise Estratégica de Mercado")
            
            def analisar_distribuicao(df, df_country):
                insights = []
                acoes = []
                pontos_atencao = []
                
                concentracao = df_country.head(5)['Quantidade'].sum() / len(df) * 100
                concentracao_top1 = df_country.iloc[0]['Quantidade'] / len(df) * 100
                
                total_paises = df['País'].nunique()
                cobertura_mercado = (total_paises / 195) * 100
                media_clientes = len(df) / total_paises
                
                mercados_potenciais = df_country[(df_country['Quantidade'] > media_clientes * 0.5) & 
                                               (df_country['Quantidade'] < media_clientes)]
                
                if concentracao_top1 > 40:
                    insights.append(f"Concentração significativa no mercado principal: {concentracao_top1:.1f}%")
                    acoes.append("Implementar estratégia de diversificação geográfica")
                    pontos_atencao.append("Alta dependência de mercado único")
                
                if cobertura_mercado < 20:
                    insights.append(f"Potencial de expansão geográfica (cobertura atual: {cobertura_mercado:.1f}%)")
                    acoes.append("Desenvolver plano de expansão para mercados estratégicos")
                
                if not mercados_potenciais.empty:
                    insights.append(f"Identificados {len(mercados_potenciais)} mercados com potencial de desenvolvimento")
                    acoes.append("Fortalecer presença em mercados emergentes")
                
                return {
                    'metricas': {
                        'concentracao': concentracao,
                        'cobertura': cobertura_mercado,
                        'media_clientes': media_clientes,
                        'total_paises': total_paises
                    },
                    'insights': insights,
                    'acoes': acoes,
                    'pontos_atencao': pontos_atencao
                }
            
            analise = analisar_distribuicao(df, df_country)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Análise de Mercado**")
                st.markdown(f"""
                **Indicadores Principais**
                - Concentração de Mercado: {analise['metricas']['concentracao']:.1f}%
                - Cobertura Global: {analise['metricas']['cobertura']:.1f}%
                - Volume Médio: {analise['metricas']['media_clientes']:.0f} clientes/país
                - Mercados Ativos: {analise['metricas']['total_paises']}
                
                **Insights Estratégicos**
                """)
                for insight in analise['insights']:
                    st.markdown(f"• {insight}")
            
            with col2:
                st.markdown("**Direcionamento Estratégico**")
                
                if analise['pontos_atencao']:
                    st.warning("Pontos Críticos")
                    for ponto in analise['pontos_atencao']:
                        st.markdown(f"• {ponto}")
                
                st.markdown("**Recomendações Estratégicas**")
                for i, acao in enumerate(analise['acoes'], 1):
                    st.markdown(f"{i}. {acao}")
                
                st.markdown(f"""
                **Horizonte de Planejamento**
                Análise gerada em: {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}
                """)

    with tab2:
        st.header("Análise Temporal")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if 'Data_Cadastro' not in df.columns:
                df['Data_Cadastro'] = pd.date_range(
                    start='2023-01-01', 
                    periods=len(df), 
                    freq='D'
                )
            
            df_temporal = df.groupby(df['Data_Cadastro'].dt.strftime('%Y-%m'))\
                .size().reset_index(name='Novos_Clientes')
            
            fig_crescimento = go.Figure()
            
            fig_crescimento.add_trace(go.Bar(
                x=df_temporal['Data_Cadastro'],
                y=df_temporal['Novos_Clientes'],
                name='Novos Clientes',
                marker_color='#32CD32',
                hovertemplate='Mês: %{x}<br>Novos Clientes: %{y}<extra></extra>'
            ))
            
            fig_crescimento.add_trace(go.Scatter(
                x=df_temporal['Data_Cadastro'],
                y=df_temporal['Novos_Clientes'].rolling(window=3).mean(),
                name='Tendência',
                line=dict(color='#FFD700', width=3),
                hovertemplate='Mês: %{x}<br>Média: %{y:.0f}<extra></extra>'
            ))
            
            fig_crescimento.update_layout(
                title='Crescimento Mensal de Clientes',
                xaxis_title='Mês',
                yaxis_title='Número de Clientes',
                template='plotly_dark',
                height=400,
                showlegend=True,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                )
            )
            
            st.plotly_chart(fig_crescimento, use_container_width=True)
        
        with col2:
            st.markdown("### Análise de Tendências")
            
            variacao_mensal = ((df_temporal['Novos_Clientes'].iloc[-1] / 
                               df_temporal['Novos_Clientes'].iloc[-2] - 1) * 100)
            
            st.metric(
                "Variação Mensal",
                f"{variacao_mensal:.1f}%",
                delta=f"{variacao_mensal:.1f}%",
                help="Comparação com mês anterior"
            )
            
            st.markdown("""
            ### Guia de Interpretação
            
            **Barras Verdes:**
            - Total de novos clientes por mês
            
            **Linha Dourada:**
            - Tendência de crescimento
            """)

        st.divider()
        if st.button("Analisar Crescimento", type="primary"):
            st.subheader("Análise de Crescimento")
            
            def analisar_crescimento(df_temporal):
                insights = []
                acoes = []
                pontos_atencao = []
                
                crescimento_medio = df_temporal['Novos_Clientes'].pct_change().mean() * 100
                crescimento_recente = df_temporal['Novos_Clientes'].pct_change().iloc[-1] * 100
                tendencia_3m = df_temporal['Novos_Clientes'].rolling(window=3).mean().pct_change().iloc[-1] * 100
                
                volatilidade = df_temporal['Novos_Clientes'].pct_change().std() * 100
                
                media_movel = df_temporal['Novos_Clientes'].rolling(window=3).mean()
                desvio_sazonal = (df_temporal['Novos_Clientes'] - media_movel).std()
                
                if crescimento_recente < crescimento_medio:
                    insights.append(f"Desaceleração recente: {crescimento_recente:.1f}% vs média {crescimento_medio:.1f}%")
                    acoes.append("Implementar ações de aceleração comercial")
                
                if volatilidade > 20:
                    insights.append(f"Alta volatilidade detectada ({volatilidade:.1f}%)")
                    pontos_atencao.append("Instabilidade no crescimento")
                    acoes.append("Desenvolver estratégias de estabilização")
                
                if desvio_sazonal > df_temporal['Novos_Clientes'].mean() * 0.2:
                    insights.append("Padrão sazonal significativo identificado")
                    acoes.append("Ajustar estratégias para períodos sazonais")
                
                if tendencia_3m < 0:
                    insights.append(f"Tendência negativa nos últimos 3 meses ({tendencia_3m:.1f}%)")
                    pontos_atencao.append("Reversão de tendência necessária")
                    acoes.append("Revisar estratégia de aquisição")
                
                return {
                    'metricas': {
                        'crescimento_medio': crescimento_medio,
                        'crescimento_recente': crescimento_recente,
                        'tendencia_3m': tendencia_3m,
                        'volatilidade': volatilidade
                    },
                    'insights': insights,
                    'acoes': acoes,
                    'pontos_atencao': pontos_atencao
                }
            
            analise = analisar_crescimento(df_temporal)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Diagnóstico Atual**")
                st.markdown(f"""
                **Indicadores-Chave**
                - Crescimento Médio: {analise['metricas']['crescimento_medio']:.1f}%
                - Crescimento Recente: {analise['metricas']['crescimento_recente']:.1f}%
                - Tendência Trimestral: {analise['metricas']['tendencia_3m']:.1f}%
                - Volatilidade: {analise['metricas']['volatilidade']:.1f}%
                
                **Insights Identificados**
                """)
                for insight in analise['insights']:
                    st.markdown(f"- {insight}")
            
            with col2:
                st.markdown("**Direcionamento Estratégico**")
                
                if analise['pontos_atencao']:
                    st.warning("Pontos de Atenção")
                    for ponto in analise['pontos_atencao']:
                        st.markdown(f"- {ponto}")
                
                st.markdown("**Ações Recomendadas**")
                for i, acao in enumerate(analise['acoes'], 1):
                    st.markdown(f"{i}. {acao}")
                
                st.markdown(f"""
                **Horizonte de Planejamento**
                Análise gerada em: {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}
                """)

    with tab3:
        st.header("Segmentação de Clientes")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            df_analise = df.groupby('País').agg({
                'Data_Cadastro': 'count'
            }).reset_index()
            
            df_analise = df_analise.sort_values('Data_Cadastro', ascending=False)
            
            fig_paises = px.bar(
                df_analise.head(10),
                x='País',
                y='Data_Cadastro',
                color='Data_Cadastro',
                title='Top 10 Países por Número de Clientes',
                template="plotly_dark",
                labels={
                    'País': 'País',
                    'Data_Cadastro': 'Número de Clientes'
                },
                color_continuous_scale='Viridis'
            )
            fig_paises.update_layout(height=500)
            st.plotly_chart(fig_paises, use_container_width=True)
        
        with col2:
            st.markdown("### Perfil dos Segmentos")
            
            pais_counts = df['País'].value_counts()
            
            quartis = pais_counts.quantile([0.25, 0.5, 0.75])
            
            def determinar_segmento(pais):
                if pd.isna(pais):
                    return 'Não Classificado'
                try:
                    count = pais_counts[pais]
                    if count <= quartis[0.25]:
                        return 'Bronze'
                    elif count <= quartis[0.5]:
                        return 'Prata'
                    elif count <= quartis[0.75]:
                        return 'Ouro'
                    else:
                        return 'Platina'
                except:
                    return 'Não Classificado'
            
            df['Segmento'] = df['País'].apply(determinar_segmento)
            
            fig_segments = px.pie(
                df,
                names='Segmento',
                title='Distribuição dos Segmentos de Clientes',
                color_discrete_map={
                    'Platina': '#E5E4E2',
                    'Ouro': '#FFD700',
                    'Prata': '#A7A7AD',
                    'Bronze': '#CD7F32'
                },
                template="plotly_dark"
            )
            st.plotly_chart(fig_segments)
            
            st.markdown("### Métricas Principais")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Total de Países",
                    f"{df['País'].nunique()}",
                    help="Número total de países com clientes"
                )
            
            with col2:
                st.metric(
                    "Média de Clientes por País",
                    f"{len(df) / df['País'].nunique():.0f}",
                    help="Média de clientes por país"
                )
            
            with col3:
                st.metric(
                    "Valor Médio por Segmento",
                    f"{len(df) / 4:.0f}",
                    help="Média de clientes por segmento"
                )

        st.divider()
        if st.button("Analisar Segmentação", type="primary"):
            def analisar_segmentacao(df):
                insights = []
                acoes = []
                pontos_atencao = []
                
                segmentos = {
                    seg: len(df[df['Segmento'] == seg]) / len(df) * 100 
                    for seg in ['Bronze', 'Prata', 'Ouro', 'Platina']
                }
                
                maior_seg = max(segmentos, key=segmentos.get)
                menor_seg = min(segmentos, key=segmentos.get)
                amplitude = max(segmentos.values()) - min(segmentos.values())
                
                evolucao_segmentos = df.groupby([
                    pd.Grouper(key='Data_Cadastro', freq='ME'),
                    'Segmento'
                ]).size().unstack(fill_value=0)
                
                if segmentos['Bronze'] > 40:
                    insights.append(f"Alta concentração no segmento Bronze: {segmentos['Bronze']:.1f}%")
                    acoes.append("Desenvolver programa de upgrade de segmentos")
                    pontos_atencao.append("Risco de baixo valor médio por cliente")
                
                if segmentos['Platina'] < 10:
                    insights.append(f"Baixa representatividade Platina: {segmentos['Platina']:.1f}%")
                    acoes.append("Implementar estratégia de desenvolvimento premium")
                
                if amplitude > 30:
                    insights.append(f"Alta disparidade entre segmentos: {amplitude:.1f}%")
                    acoes.append("Equilibrar distribuição entre segmentos")
                
                if evolucao_segmentos.shape[0] > 1:
                    tendencia = evolucao_segmentos.pct_change().mean()
                    seg_crescente = tendencia.idxmax()
                    seg_decrescente = tendencia.idxmin()
                    
                    if tendencia[seg_decrescente] < -0.1:
                        insights.append(f"Segmento {seg_decrescente} em declínio")
                        pontos_atencao.append(f"Reversão necessária em {seg_decrescente}")
                
                return {
                    'metricas': {
                        'segmentos': segmentos,
                        'amplitude': amplitude,
                        'maior_seg': maior_seg,
                        'menor_seg': menor_seg
                    },
                    'insights': insights,
                    'acoes': acoes,
                    'pontos_atencao': pontos_atencao
                }
            
            analise = analisar_segmentacao(df)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Diagnóstico Atual**")
                st.markdown(f"""
                **Métricas por Segmento**
                """)
                for seg, valor in analise['metricas']['segmentos'].items():
                    st.markdown(f"- {seg}: {valor:.1f}%")
                
                st.markdown("""
                **Insights Identificados**
                """)
                for insight in analise['insights']:
                    st.markdown(f"- {insight}")
            
            with col2:
                st.markdown("**Direcionamento Estratégico**")
                
                if analise['pontos_atencao']:
                    st.warning("Pontos de Atenção")
                    for ponto in analise['pontos_atencao']:
                        st.markdown(f"- {ponto}")
                
                st.markdown("**Ações Recomendadas**")
                for i, acao in enumerate(analise['acoes'], 1):
                    st.markdown(f"{i}. {acao}")
                
                st.markdown(f"""
                **Horizonte de Planejamento**
                Análise gerada em: {datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M')}
                """)

    st.divider()
    
    