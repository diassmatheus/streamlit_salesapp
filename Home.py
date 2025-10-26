import pandas as pd
from pathlib import Path
import streamlit as st
import plotly.express as px
from datetime import datetime, date, timedelta

st.set_page_config(layout="wide")

st.markdown('# Bem vindo ao analisador de vendas')
st.divider()

st.markdown(
    '''
    O Analisador de Vendas é uma ferramenta interativa que ajuda equipes e gestores 
    a visualizar resultados e identificar tendências de vendas de forma rápida e intuitiva. 
    Permite acompanhar indicadores por período, filial, produto e vendedor, 
    além de gerar análises personalizadas e registrar novas vendas em tempo real.

     Desenvolvido em **Python**, foram utilizadas três principais bibliotecas neste projeto:

    - `pandas`: para manipulação de dados
    - `plotly`: para visualização de dados
    - `streamlit`: para criação desse webApp interativo que você se encontra nesse momento

    O projeto combina manipulação eficiente de dados e visualizações dinâmicas em uma interface leve e modular. 
    A estrutura em múltiplas páginas e o uso de mecanismos de cache e reaproveitamento de dados garantem desempenho, 
    consistência e fácil expansão do aplicativo.

    Os dados utilizados foram gerados pelo script [gerador_de_vendas.py](https://github.com/diassmatheus/streamlit_salesapp/blob/main/datasets/gerador_de_vendas.py), 
    e podem ser visualizados na aba **Dados Brutos**.
    '''
            )


st.sidebar.markdown('Desenvolvido por [Matheus Dias](https://diassmatheus.github.io/)')