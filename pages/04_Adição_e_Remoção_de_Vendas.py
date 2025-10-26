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

st.markdown('# Adição e Remoção de Vendas')

col1, col2 = st.columns([0.3, 0.7])

adicionar_ou_remover = col1.selectbox('Deseja acionar ou remover venda?', ['Adicionar', 'Remover'])

if adicionar_ou_remover == 'Adicionar':
    col1.markdown('#### Adição de venda')

    filiais = list(df_filiais['cidade'].unique())
    filial_selecionada = col1.selectbox('Selecione a filial:',filiais)

    vendedores = list(df_filiais.loc[df_filiais['cidade'] == filial_selecionada, 'vendedores'].iloc[0].strip('][]').replace("'","").split(', '))
    vendedor_selecionado = col1.selectbox('Selecione o vendedor:', vendedores)

    produtos = list(df_produtos['nome'].unique())
    produto_selecionado = col1.selectbox('Selecione o produto:', produtos)

    nome_cliente = col1.text_input('Nome do cliente:')

    genero_selecionado = col1.selectbox('Gênero do cliente:', ['masculino', 'feminino'])

    forma_pagamento_selecionada = col1.selectbox('Selecione a forma de pagamento:', ['credito', 'boleto', 'pix'])

    adicionar_venda = col1.button('Adicionar venda')
    if adicionar_venda:
        lista_adicionar = [df_vendas['id_venda'].max() + 1,
                        filial_selecionada,
                        vendedor_selecionado,
                        produto_selecionado,
                        nome_cliente,
                        genero_selecionado,
                        forma_pagamento_selecionada]
        hora_adicionar = datetime.now()
        df_vendas.loc[hora_adicionar] = lista_adicionar
        caminho_arquivo = Path(__file__).resolve().parent.parent / 'datasets' / 'vendas.csv'
        df_vendas.to_csv(caminho_arquivo, sep=';', decimal=',')

elif adicionar_ou_remover == 'Remover':

    col1.markdown('#### Remoção de vendas')

    id_remocao = col1.number_input('Digite o ID da venda que deseja remover:', 0, df_vendas['id_venda'].max())

    remover_venda = col1.button('Remover venda')
    if remover_venda:
        df_vendas = df_vendas[df_vendas['id_venda'] != id_remocao]
        caminho_arquivo = Path(__file__).resolve().parent.parent / 'datasets' / 'vendas.csv'
        df_vendas.to_csv(caminho_arquivo, sep=';', decimal=',')

df_vendas_ordenado = df_vendas.sort_values(by='id_venda', ascending=False)
col2.markdown('#### Tabela de vendas')
col2.dataframe(df_vendas_ordenado, height=800)

st.sidebar.markdown('Desenvolvido por [Matheus Dias](https://diassmatheus.github.io/)')