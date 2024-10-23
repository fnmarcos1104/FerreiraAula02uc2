import os 

os.system('cls')


import pandas as pd


import numpy as np

casas = [150000, 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000]
mediana = np.median(casas)
print(f'Valor mediano das casas R${mediana}')

media = np.mean(casas)
print(f'Valor médio das casas R${media}')

print(f'O valor mais representativo é o de mediana R${mediana}. Pois o valor de uma das casas é fora do comum dos demais.')