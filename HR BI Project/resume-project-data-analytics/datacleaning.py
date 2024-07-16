#%% 
import pandas as pd

# Load Excel sheets
june = pd.read_excel(io=r"C:\Users\Luiz_Ang_2002\Documents\Kaggle\HR BI Project\resume-project-data-analytics\Attendance Sheet 2022-2023_Masked.xlsx", sheet_name="June 2022")
may = pd.read_excel(io=r"C:\Users\Luiz_Ang_2002\Documents\Kaggle\HR BI Project\resume-project-data-analytics\Attendance Sheet 2022-2023_Masked.xlsx", sheet_name="May 2022")
april = pd.read_excel(io=r"C:\Users\Luiz_Ang_2002\Documents\Kaggle\HR BI Project\resume-project-data-analytics\Attendance Sheet 2022-2023_Masked.xlsx", sheet_name="Apr 2022")
#%%
def cleaning(df):
    df.columns = df.iloc[0]  # Set the first row as the column headers
    df = df[1:]  # Remove the first row
    df.reset_index(drop=True, inplace=True)  # Reset the index
    df = df.iloc[:, :33]  # Select the first 33 columns
    df = df.melt(id_vars=['Employee Code', 'Name'], var_name='date', value_name='presence')  # Melt the DataFrame
    df.reset_index(drop=True, inplace=True)  # Reset the index after melting
    return df  # Return the cleaned DataFrame
#%%
lista = [june,april,may]
#%%
for x in lista:
    x = cleaning(x)
# %%
april.head()
# %%
april = pd.read_excel(io=r"C:\Users\Luiz_Ang_2002\Documents\Kaggle\HR BI Project\resume-project-data-analytics\Attendance Sheet 2022-2023_Masked.xlsx", sheet_name="Apr 2022")
