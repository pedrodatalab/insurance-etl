#%%
#Import librarys

import pandas as pd
import datetime
import os 

# Load dos arquivos a serem tratados
df_policies = pd.read_csv(r"E:\Estudos\Projects\Insurance_etl\policies.csv", sep =",")
df_claims = pd.read_csv(r"E:\Estudos\Projects\Insurance_etl\claims.csv", sep =",")


#%%
#Checando as colulas de data para saber se tem campos nulos
df_policies[['start_date', 'end_date']].isnull().sum()

#%%

df_claims['date'].isnull().sum()
# %%

#Conversao das datas de YYYY-MM-DD para DD-MM-YYYY

df_policies.head()
# %%

df_policies['start_date'].dtype
df_claims['date'].dtype
#%%
#Conversao das colunas start_date e end_date para datetime

df_policies['start_date'] = pd.to_datetime(df_policies['start_date'], errors='coerce')
df_policies['end_date'] = pd.to_datetime(df_policies['end_date'], errors='coerce')
df_policies['start_date'].dtype

# %%
df_policies['start_date'].dt.strftime('%d-%m-%Y')
df_policies.head()
# %%

#Conversao das datas de YYYY-MM-DD para DD-MM-YYYY - converte do tipo datetime para um string, não podendo fazer novas operações

# df_policies['start_date'] = df_policies['start_date'].dt.strftime('%d-%m-%Y')
# df_policies['end_date'] = df_policies['end_date'].dt.strftime('%d-%m-%Y')

