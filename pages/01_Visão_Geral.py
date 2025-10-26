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

st.sidebar.markdown('## Filtros')

data_inicial = st.sidebar.date_input('Data inicial:', df.index.date.max() - timedelta(days=30), min_value=df.index.date.min(), max_value=df.index.date.max())
data_final = st.sidebar.date_input('Data final:', df.index.date.max(), min_value=df.index.date.min(), max_value=df.index.date.max())

st.markdown('# Dashboard de vendas')

df_filtrado = df[(df.index.date >= data_inicial) & (df.index.date <= data_final)]
df_filtrado_mes_anterior = df[(df.index.date >= data_inicial - timedelta(days=30)) & (df.index.date <= data_final - timedelta(days=30))]

col11, col12 = st.columns(2)

valor_geral_vendas = df_filtrado['preco'].sum()
valor_geral_formatado = f"R${valor_geral_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
delta_valor_vendas = df_filtrado['preco'].sum() - df_filtrado_mes_anterior['preco'].sum()
delta_valor_vendas_formatado = f"R${delta_valor_vendas:,.2f} (variação mensal)".replace(",", "X").replace(".", ",").replace("X", ".")
col11.metric(label='Valor de vendas no período', value=valor_geral_formatado, delta=delta_valor_vendas_formatado)

quantidade_geral_vendas = df_filtrado['preco'].count()
quantidade_geral_formatado = f"{quantidade_geral_vendas:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
delta_quantidade_vendas = df_filtrado['preco'].count() - df_filtrado_mes_anterior['preco'].count()
delta_quantidade_vendas_formatado = f"{delta_quantidade_vendas:,.0f} (variação mensal)".replace(",", "X").replace(".", ",").replace("X", ".")
col12.metric(label='Qtde de vendas no período', value=quantidade_geral_formatado, delta=delta_quantidade_vendas_formatado)

col21, col22 = st.columns(2)

principal_filial = df_filtrado.groupby('filial')['preco'].agg('sum').sort_values(ascending=False).index[0]
col21.metric('Principal filial', principal_filial)

principal_vendedor = df_filtrado.groupby('vendedor')['preco'].agg('sum').sort_values(ascending=False).index[0]
col22.metric('Principal vendedor', principal_vendedor)

st.divider()

col31, col32 = st.columns(2)

df_filtrado['dia_venda'] = df_filtrado.index.date
vendas_dia = df_filtrado.groupby('dia_venda')['preco'].agg('sum')
vendas_dia.name = 'Valor vendas'
fig1 = px.line(vendas_dia)
col31.plotly_chart(fig1)

selecao_keys = {'Forma de Pagamento': 'forma_pagamento',
                'Gênero Cliente': 'cliente_genero',
                'Produto': 'produto',
                'Filial': 'filial',
                'Vendedor': 'vendedor'}
analise_selecionada = st.sidebar.selectbox('Variável gráfico de pizza:', list(selecao_keys.keys()))
analise_selecionada = selecao_keys[analise_selecionada]

fig2 = px.pie(df_filtrado, names=analise_selecionada, values='preco')
col32.plotly_chart(fig2)

st.divider()

st.sidebar.divider()
st.sidebar.markdown('Desenvolvido por [Matheus Dias](https://diassmatheus.github.io/)')