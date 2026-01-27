# Análise de Dados Industriais
"""
Vamos trabalhar com dados fícticios de sensores de máquinas industriais. A ideia é simular um conjunto de medições
para estruturar nosso DataFrame e fazer análises futuras.
"""

# Importando bibliotecas principais
import pandas as pd     # Manipulação de tabelas
import matplotlib.pyplot as plt     # Visualização Simples

# Criando o "dicionário" com os dados
dados = pd.DataFrame({
    "maquina" : ["A", "A", "B", "B", "C", "C"],
    "dia" : [1, 2, 1, 2, 1, 2],
    "temperatura": [68.5, 70.1, 72.3, 73.0, 71.8, 70.5]
})

# Transformando em DataFrame
df_dados = pd.DataFrame(dados)

# Visualização do DataFrame
print(df_dados.head())

# Verificando as colunas 
print(df_dados.columns)

# Verificando os tipos de dados de cada colunas
print(df_dados.dtypes)

# Resumo geral do DataFrame
print(df_dados.info())