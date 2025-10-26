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

df_produtos2 = df_produtos.rename(columns={'nome':'produto'})
df = pd.merge(left=df_vendas.reset_index(), right=df_produtos2[['produto','preco']], on='produto', how='left')
df.set_index('data', inplace=True)
df['comissao'] = df['preco'] * comissao

st.markdown('# Tabela Dinâmica')

colunas_analise = ['filial', 'vendedor', 'produto', 'cliente_genero', 'forma_pagamento']
colunas_numericas = {'preço':'preco', 'comissão':'comissao'}

col11, col12 = st.columns(2)

indices_dinamica = col11.multiselect(label='Selecione os índices:', options=colunas_analise)
colunas_analise_filtradas = [c for c in colunas_analise if c not in indices_dinamica] 
colunas_dinamica = col12.multiselect(label='Selecione as colunas:', options=colunas_analise_filtradas)

valor_analise = col11.selectbox(label='Selecione o valor da análise:', options=list(colunas_numericas.keys()))

funcoes_agregacao ={'soma':'sum', 'contagem':'count'}
metrica_analise = col12.selectbox(label='Selecione a métrica da análise:', options=list(funcoes_agregacao.keys()))

if len(indices_dinamica) > 0 and len(colunas_dinamica) > 0:
    metrica = funcoes_agregacao[metrica_analise]
    valor = colunas_numericas[valor_analise]
    tabela_dinamica = pd.pivot_table(data=df,
                                    index=indices_dinamica,
                                    columns=colunas_dinamica,
                                    values=valor,
                                    aggfunc=metrica,
                                    margins=True,
                                    margins_name='Total')
    st.markdown('## Tabela dinâmica')
    st.dataframe(tabela_dinamica)
else:
    st.warning("Selecione pelo menos um índice e uma coluna para gerar a tabela dinâmica.")

st.sidebar.markdown('Desenvolvido por [Matheus Dias](https://diassmatheus.github.io/)')