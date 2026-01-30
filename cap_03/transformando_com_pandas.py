# Importação das Bibliotecas
import pandas as pd

# DataFrame
data_frame = pd.DataFrame({
    'maquina' : ['M1', 'M2', 'M1', 'M3', 'M2', 'M1', 'M3', 'M2'],
    'setor' : ['usinagem', 'pintura', 'usinagem', 'usinagem', 'usinagem', 'montagem', 'pintura', 'usinagem'],
    'temperatura': [85, 78, 90, 88, 95, 80, 75, 100],
    'tempo_operacao': [120, 110, 130, 115, 140, 125, 100, 135]
})

# 2ª DataFrame
data_frame_status = pd.DataFrame({
    'maquina': ['M1', 'M2', 'M3'],
    'status' : ['ativa', 'manutenção', 'ativa']
})

# print(data_frame)

# Filtros usinagem e temperatura > 80º C
df_filtrado = data_frame[(data_frame['setor'] == 'usinagem') & 
                        (data_frame['temperatura'] > 80)]

# print(df_filtrado)

# Agrupamento tempo médio de operação por máquinas
df_agrupado = data_frame.groupby('maquina')['tempo_operacao'].mean().reset_index()

# Tempo médio de operações de máquinas
# print(df_agrupado)

# Junção de dataframe
df_completo = pd.merge(data_frame, data_frame_status, on='maquina', how='left')

print(df_completo)