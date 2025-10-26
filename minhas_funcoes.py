import pandas as pd
from pathlib import Path
import streamlit as st

def leitura_dados():
    if not 'dados' in st.session_state:
        pasta_datasets = Path(__file__).resolve().parent / 'datasets'
        df_vendas = pd.read_csv(pasta_datasets / 'vendas.csv', sep=';', decimal=',', index_col=0, parse_dates=True)
        df_filiais = pd.read_csv(pasta_datasets / 'filiais.csv', sep=';', decimal=',', index_col=0)
        df_produtos = pd.read_csv(pasta_datasets / 'produtos.csv', sep=';', decimal=',', index_col=0)
        dados = {'df_vendas':df_vendas, 'df_filiais':df_filiais, 'df_produtos':df_produtos}
        st.session_state['dados'] = dados