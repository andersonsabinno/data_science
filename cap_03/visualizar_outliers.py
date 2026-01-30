# Importação das Bibliotecas
import pandas as pd
import matplotlib.pyplot as plt


# Criando DataFrame
df = pd.DataFrame({
    'temperatura' : [22.5, 22.8, 23.0, 22.6, 22.7, 23.5, 22.9, 23.1, 22.4, 22.6, 50.0, -10.0],
    'pressao' : [1.21, 1.22, 1.19, 1.20, 1.23, 1.18, 1.20, 1.21, 1.19, 1.22, 1.21, 1.20],
    'tempo_processamento' : [120, 110, 130, 115, 125, 300, 118, 122, 119, 117, 124, 116]
})

# Visualização dos outliers
plt.figure(figsize=(12, 8))

# Boxplots
plt.subplot(2, 3, 1)
df.boxplot(column='temperatura')
plt.title("Boxplot - Temperatura")
plt.subplot(2, 3 , 2)
df.boxplot(column='pressao')
plt.title("Boxplot - Pressão")
plt.subplot(2, 3, 3)
df.boxplot(column='tempo_processamento')
plt.title("Boxplot - Tempo de Processamento")

# Histogramas
plt.subplot(2, 3, 4)
df['temperatura'].hist(bins=20)
plt.title("Histograma - Temperatura")
plt.subplot(2, 3, 5)
df['pressao'].hist(bins=10)
plt.title("Histograma - Pressão")
plt.subplot(2, 3, 6)
df['tempo_processamento'].hist(bins=15)
plt.title("Histograma - Tempo de Processamento")

plt.tight_layout()
plt.show()