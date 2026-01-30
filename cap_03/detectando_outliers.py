# Importação das Bibliotecas
import pandas as pd

# Criando DataFrame
df = pd.DataFrame({
    'temperatura' : [22.5, 22.8, 23.0, 22.6, 22.7, 23.5, 22.9, 23.1, 22.4, 22.6, 50.0, -10.0],
    'pressao' : [1.21, 1.22, 1.19, 1.20, 1.23, 1.18, 1.20, 1.21, 1.19, 1.22, 1.21, 1.20],
    'tempo_processamento' : [120, 110, 130, 115, 125, 300, 118, 122, 119, 117, 124, 116]
})


# 2. Método do InterQuartil (IQR)
q1 = df['temperatura'].quantile(0.25)
q3 = df['temperatura'].quantile(0.75)

# ignorando os valores extremos
iqr = q3 - q1

limite_inferior_iqr = q1 - 1.5 * iqr
limite_superior_iqr = q3 + 1.5 * iqr

outliers_iqr = df[(df['temperatura'] < limite_inferior_iqr) |
                  (df['temperatura'] > limite_superior_iqr)]

print('Outliers da coluna temperatura: ')
print(outliers_iqr)