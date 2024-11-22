"""
Module to displayed all data
"""
import streamlit as st

from customer_management.utils.layer_controller import run_data_pipeline
from customer_management.utils.transform_excel import convert_df_to_excel

st.set_page_config(layout="wide")
st.title("Customer Data Pipeline")
st.write("As informações abaixo são atualizadas automaticamente ao carregar a página.")

st.info("Executando o pipeline... Isso pode levar alguns segundos.")
df_gold = run_data_pipeline()

st.success("Pipeline concluído com sucesso!")
st.write("Visualização dos dados processados:")

st.dataframe(df_gold, height=800, width=2000)

excel_file = convert_df_to_excel(df_gold)

st.download_button(
    label="Baixar Dados Processados (Excel)",
    data=excel_file,
    file_name="gold_layer.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)
