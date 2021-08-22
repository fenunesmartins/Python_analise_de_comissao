# Solução:

# 1. Abrir os 6 arquivos do excel;
# 2. Para cada arquivo, verificar se algum valor na coluna de vendas seja maior do que 55.000
# 3. > 55.000 envia SMS com o Nome, Mês e as vendas do vendedor, se não for maior o programa para



import pandas as pd
import openpyxl as xls
import os
from twilio.rest import Client

account_sid = 'AC13a05e5b30717f3a34700abf6e65568b'
auth_token = '8a63bb0cfbc2648fa317f4eb8d2f0cdc'

lista_meses = ['janeiro', 'fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(mes + '.xlsx')
    #print(tabela_vendas)

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'Encontrado mo mes de {mes} com mais de 55000. Vendedor:{vendedor} , Vendas{vendas}')
    else:
        print('Não encontrado')




client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="f'Encontrado mo mes de {mes} com mais de 55000. Vendedor:{vendedor} , Vendas{vendas}'",
                     from_='3204039070',
                     to='5511973605501'
                 )

print(message.sid)
