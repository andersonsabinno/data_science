# Limpeza de dados

 > conversão de tipos de dados > tratamentos de valores nulos > padronização de formatos e textos

**drop()** é diferente de **dropna()**, o primeiro remove uma coluna e o segundo remove as linhas com valores nulos. Caso, eu queria remover colunas com valores nulos **dropna(axis=1)**.

Substituo os valores nulos por zero nas colunas, **df_dados.fillna(0)**.