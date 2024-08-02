#%% 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# %%
control = pd.read_csv(r"C:\Users\luiz.angelo\Documents\VSCODE\personal_projects\AB Testing\archive (2)\control_group.csv",sep=";")
test = pd.read_csv(r"C:\Users\luiz.angelo\Documents\VSCODE\personal_projects\AB Testing\archive (2)\test_group.csv",sep=";")
#%%
test.info()
# %%
control.info()
#%%
dataframes = [test,control]
for i,data in enumerate(dataframes):
    data['Date'] = pd.to_datetime(data['Date'], format='%d.%m.%Y')
    i = data.info()
#%%
control.describe().round(2)
#%%
test.describe().round(2)
#%%
# %%
def histograma(x: pd.DataFrame, y: str, df_name: str):
    '''
    Função para criar histogramas.
    
    Parâmetros:
    x (pd.DataFrame): DataFrame contendo os dados.
    y (str): Nome da coluna do DataFrame a ser plotada.
    df_name (str): Nome do DataFrame a ser exibido no título.
    '''
    plt.figure(figsize=(10, 6))
    plt.hist(x[y],edgecolor='k')  # Adding bins and edgecolor for better visualization
    plt.xlabel(y)
    plt.ylabel('Frequência')
    plt.title(f'Histograma do DataFrame {df_name} da coluna {y}')
    plt.show()

dataframes = [(test,'teste'),(control,'controle')]
colunas = list(columns)

# Gerando histogramas
for data, name in dataframes:
    for col in colunas:
        histograma(data, col, name)

# %%
