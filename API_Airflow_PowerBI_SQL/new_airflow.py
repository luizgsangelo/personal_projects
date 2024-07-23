#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados de exemplo
data = {'Categoria': ['A', 'B', 'C', 'D', 'E'],
        'Frequência': [50, 30, 20, 15, 10]}
df = pd.DataFrame(data)

# Calcular a frequência acumulada
df = df.sort_values(by='Frequência', ascending=False)
df['Frequência Acumulada'] = df['Frequência'].cumsum()
df['Frequência Acumulada (%)'] = df['Frequência Acumulada'] / df['Frequência'].sum() * 100

# Criar o gráfico de Pareto
fig, ax1 = plt.subplots()

# Gráfico de barras para a frequência absoluta
sns.barplot(x='Categoria', y='Frequência', data=df, ax=ax1, color='b')

# Adicionar rótulos ao eixo y
ax1.set_ylabel('Frequência', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Criar um segundo eixo y para a frequência acumulada
ax2 = ax1.twinx()
ax2.plot(df['Categoria'], df['Frequência Acumulada (%)'], color='r', marker='o', linestyle='-')
ax2.set_ylabel('Frequência Acumulada (%)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Definir os limites do eixo y secundário de 0 a 100
ax2.set_ylim(0, 100)

# Adicionar um título ao gráfico
plt.title('Gráfico de Pareto')

# Mostrar o gráfico
plt.show()

# %%
