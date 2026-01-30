# Importação das Bibliotecas
import pandas as pd


# Criando DataFrame
df = pd.DataFrame({
    'temperatura' : [22.5, 22.8, 23.0, 22.6, 22.7, 23.5, 22.9, 23.1, 22.4, 22.6, 50.0, -10.0],
    'pressao' : [1.21, 1.22, 1.19, 1.20, 1.23, 1.18, 1.20, 1.21, 1.19, 1.22, 1.21, 1.20],
    'tempo_processamento' : [120, 110, 130, 115, 125, 300, 118, 122, 119, 117, 124, 116]
})

#print(df.describe())

# Detectando outliers na coluna temperatura
# 1. Método de Desvio
media = df['temperatura'].mean() # média
desvio = df['temperatura'].std() # desvio padrão

# valores distantes da média com mais de 3 desvios padrão
limite_inferior_std = media - 3 * desvio 
limite_superior_std = media + 3 * desvio

outliers_std = df[(df['temperatura'] < limite_inferior_std) |
                  (df['temperatura'] > limite_superior_std)]

# print('Outliers na coluna temperatura: ')
print(outliers_std)