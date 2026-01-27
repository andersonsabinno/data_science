import pandas as pd

dados_csv = pd.read_csv('cap_02/dados_ficticios.csv', sep=',', encoding='utf-8')

print(dados_csv.head())
print(dados_csv.info())
print(dados_csv.describe())