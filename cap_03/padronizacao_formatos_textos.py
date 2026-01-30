# Importação da Biblioteca
import pandas as pd

# Criando DataFrame
df_dados = pd.DataFrame({
    'resposta_checklist' : ['Sim', 'sim', 'SIM', 'Sim', 'sIm'],
    'data_leitura' : ['2023-10-01', '01/10/2023', '10/01/23', 'erro', '']
})

# print(df_dados.info())

# Padronizando textos
df_dados = df_dados['resposta_checklist'].str.lower().str.strip()

# print(df_dados)

# Padronizando data
df_dados['data_leitura'] = pd.to_datetime(df_dados['data_leitura'], errors='coerce')

# print(df_dados)