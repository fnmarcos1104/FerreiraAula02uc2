import os 

os.system('cls')


import pandas as pd


import numpy as np


df = pd.read_excel('vendas_roupas1.xlsx')
# print(df)

categoria = df['Categoria']
quantidade_vendida = df['Quantidade Vendida']
print(quantidade_vendida.unique())
print(categoria.unique())

q1 = np.quantile(quantidade_vendida, 0.25)
q2 = np.quantile(quantidade_vendida, 0.50)
q3 = np.quantile(quantidade_vendida, 0.75)

# print(f'Q1: {q1}')
# print(f'Q2: {q2}')
# print(f'Q3: {q3}')


mediana = np.median(quantidade_vendida)
# print(f'Mediana de quantidade vendida {mediana}')

media = np.mean(quantidade_vendida)
# print(f'Média de quantidade vendida {media}')

qtdvdd_organizada = df.sort_values(by='Quantidade Vendida', ascending=True)
quantidade_vendida = qtdvdd_organizada['Quantidade Vendida']
print(quantidade_vendida.values)
