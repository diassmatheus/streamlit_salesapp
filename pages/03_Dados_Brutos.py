import pandas as pd
from pathlib import Path
import streamlit as st
import plotly.express as px
from datetime import datetime, date, timedelta
from minhas_funcoes import leitura_dados

st.set_page_config(layout="wide")

comissao = 0.08

leitura_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_filiais = st.session_state['dados']['df_filiais']
df_produtos = st.session_state['dados']['df_produtos']

st.markdown('# Dados Brutos')

col1, col2 = st.columns([0.3, 0.7])

col1.markdown('#### Seleção de tabelas')

tabela_selecionada = col1.selectbox('Selecione a tabela que você deseja ver:', ['Vendas', 'Produtos', 'Filiais'])

if tabela_selecionada == 'Produtos':
    col2.markdown('### Tabela de Produtos')
    col2.dataframe(df_produtos)

elif tabela_selecionada == 'Filiais':
    col2.markdown('### Tabela de Filiais')
    col2.dataframe(df_filiais)

elif tabela_selecionada == 'Vendas':
    col2.markdown('### Tabela de Vendas')

    col1.markdown('#### Filtrar tabela')
    colunas_selecionadas = col1.multiselect('Selecione as colunas da tabela:', list(df_vendas.columns), list(df_vendas.columns))

    coluna_filtro = col1.selectbox('Filtrar coluna:', colunas_selecionadas)
    valor_filtro = col1.selectbox('Valor do filtro:', list(df_vendas[coluna_filtro].unique()))
    col11, col12 = col1.columns(2)
    filtrar = col11.button('Filtrar')
    limpar = col12.button('Limpar')

    if filtrar:
        col2.dataframe(df_vendas.loc[df_vendas[coluna_filtro] == valor_filtro, colunas_selecionadas], height=800)
    elif limpar:
        col2.dataframe(df_vendas[colunas_selecionadas], height=800)
    else:
        col2.dataframe(df_vendas[colunas_selecionadas], height=800)


st.sidebar.markdown('Desenvolvido por [Matheus Dias](https://diassmatheus.github.io/)')