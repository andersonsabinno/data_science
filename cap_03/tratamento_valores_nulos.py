# Importação de bibliotecas
import pandas as pd
import numpy as np 

# Criando o DataFrame com valores ausentes
df_dados = pd.DataFrame({
    'temperatura' : [22.5, np.nan, 24.1, 23.0, np.nan, 25.3, 26.1], 
    'pressao' : [1.2, 1.5, np.nan, 1.4, 1.3, np.nan, np.nan], 
    'vibracao' : [0.5, 0.7, 0.6, np.nan, 0.9, 0.8, 1.0]
})

# Remove todas as linhas que tenham valores nulos
df_dados_drop_linhas = df_dados.dropna()

# Remove colunas com valores nulos
df_dados_drop_colunas = df_dados.dropna(axis=1)

# Mantem as linhas na qual a coluna temperatura não tem valores nulos
df_filtrado = df_dados[df_dados['temperatura'].notnull()]

# print(df_filtrado)

# Adiciona 0 em valores nulos
df_zero = df_dados.fillna(0)

# Preencher os nulos da coluna 'pressão' com média da própria coluna
df_media = df_dados.copy()
df_media['pressao'] = df_media['pressao'].fillna(df_media['pressao'].mean()) 

# Visualização com os dados nulos sobrescritos com a média da coluna
print(df_media)