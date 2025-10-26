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

st.sidebar.markdown('## Seleção de tabelas')

tabela_selecionada = st.sidebar.selectbox('Selecione a tabela que você deseja ver:', ['Vendas', 'Produtos', 'Filiais'])

if tabela_selecionada == 'Produtos':
    st.markdown('### Tabela de Produtos')
    st.dataframe(df_produtos)

elif tabela_selecionada == 'Filiais':
    st.markdown('### Tabela de Filiais')
    st.dataframe(df_filiais)

elif tabela_selecionada == 'Vendas':
    st.markdown('### Tabela de Vendas')

    st.sidebar.markdown('### Filtrar tabela')
    colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas da tabela:', list(df_vendas.columns), list(df_vendas.columns))

    col1, col2 = st.sidebar.columns(2)
    coluna_filtro = col1.selectbox('Filtrar coluna:', colunas_selecionadas)
    valor_filtro = col2.selectbox('Valor do filtro:', list(df_vendas[coluna_filtro].unique()))
    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')

    if filtrar:
        st.dataframe(df_vendas.loc[df_vendas[coluna_filtro] == valor_filtro, colunas_selecionadas])
    elif limpar:
        st.dataframe(df_vendas[colunas_selecionadas])
    else:
        st.dataframe(df_vendas[colunas_selecionadas])


st.sidebar.divider()
st.sidebar.markdown('Desenvolvido por [Matheus Dias](https://diassmatheus.github.io/)')