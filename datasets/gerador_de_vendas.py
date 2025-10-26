import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

FILIAIS = [{'estado': 'SP',
            'cidade': 'São Paulo',
            'vendedores': ['João Silva', 'Maria Souza']},

            {'estado': 'SP',
            'cidade': 'Guarulhos',
            'vendedores': ['Pedro Santos', 'Ana Oliveira']},

            {'estado': 'SP',
            'cidade': 'Osasco',
            'vendedores': ['Lucas Lima', 'Juliana Costa']},

            {'estado': 'SP',
            'cidade': 'Diadema',
            'vendedores': ['Rafael Alves', 'Fernanda Ribeiro']},

            {'estado': 'SP',
            'cidade': 'São Bernardo do Campo',
            'vendedores': ['Carla Pereira', 'Marcos Fernandes']},
            
            {'estado': 'SP',
            'cidade': 'Santo André',
            'vendedores': ['Bruno Rocha', 'Patrícia Gomes']}]

PRODUTOS = [{'nome': 'Smart TV 50" 4K',
             'id': 0,
             'preco': 2999.00},

            {'nome': 'Notebook i5 8GB SSD 512GB',
             'id': 1,
             'preco': 3799.00},

            {'nome': 'Smartphone 5G 128GB',
             'id': 2,
             'preco': 2499.00},

            {'nome': 'Caixa de Som Bluetooth',
             'id': 3,
             'preco': 349.00}]

GENEROS_CLIENTES = ['male', 'female']
FORMA_PAGAMENTO = ['pix', 'dinheiro', 'boleto', 'debito'] + ['credito'] * 8


vendas = []
for _ in range(6000):
    filial = random.choice(FILIAIS)
    vendedor = random.choice(filial['vendedores'])
    produto = random.choice(PRODUTOS)
    hora_venda = datetime.now() - timedelta(days=random.randint(1, 750), hours=random.randint(-5, 5), minutes=random.randint(-30, 30))
    genero_cliente = random.choice(GENEROS_CLIENTES)
    nome_cliente = names.get_full_name(genero_cliente)
    forma_pagamento = random.choice(FORMA_PAGAMENTO)
    vendas += [{'data': hora_venda, 
                'id_venda': 0, 
                'filial': filial['cidade'], 
                'vendedor': vendedor, 
                'produto': produto['nome'],
                'cliente_nome': nome_cliente,
                'cliente_genero': genero_cliente.replace('female', 'feminino').replace('male', 'masculino'),
                'forma_pagamento': forma_pagamento,
                }]

df_vendas = pd.DataFrame(vendas).set_index('data').sort_index()
df_vendas['id_venda'] = [i for i in range(len(df_vendas))]
df_filiais = pd.DataFrame(FILIAIS)
df_produtos = pd.DataFrame(PRODUTOS)

pasta_atual = Path(__file__).parent

df_vendas.to_csv(pasta_atual / 'vendas.csv', decimal=',', sep=';')
df_filiais.to_csv(pasta_atual / 'filiais.csv', decimal=',', sep=';')
df_produtos.to_csv(pasta_atual / 'produtos.csv', decimal=',', sep=';')

df_vendas.to_excel(pasta_atual / 'vendas.xlsx')
df_filiais.to_excel(pasta_atual / 'filiais.xlsx')
df_produtos.to_excel(pasta_atual / 'produtos.xlsx')
