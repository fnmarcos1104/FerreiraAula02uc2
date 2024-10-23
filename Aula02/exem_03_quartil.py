import os 

os.system('cls')


import pandas as pd


import numpy as np

idades = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])

q1 = np.quantile(idades, 0.25)
q2 = np.quantile(idades, 0.50)
q3 = np.quantile(idades, 0.75)

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')