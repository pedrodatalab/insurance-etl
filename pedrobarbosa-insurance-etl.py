#%%
#Import librarys
import sys
print(sys.executable)

import pandas as pd
import datetime
import fastparquet

#%%
# Load dos arquivos a serem tratados
df_policies = pd.read_csv(r"E:\Estudos\Projects\Insurance_etl\policies.csv", sep =",")
df_claims = pd.read_csv(r"E:\Estudos\Projects\Insurance_etl\claims.csv", sep =",")

#%%
df_policies.head()
#%%
#Checando as colulas de data para saber se tem campos nulos
df_policies[['start_date', 'end_date']].isnull().sum()

#%%

df_claims['date'].isnull().sum()
# %%

#Checando o tipo da coluna

df_policies['start_date'].dtype
df_claims['date'].dtype
#%%
# Renomeando a coluna data do df_claims
df_claims.rename(columns={'date': 'claim_date'}, inplace=True)
df_claims.head()

#%%
#Conversao das colunas start_date e end_date para datetime - df_policies

df_policies['start_date'] = pd.to_datetime(df_policies['start_date'], errors='coerce')
df_policies['end_date'] = pd.to_datetime(df_policies['end_date'], errors='coerce')
df_policies['start_date'].dtype
#%%
#Conversao da colunas claim_date para datetime - df_policies

df_claims['claim_date'] = pd.to_datetime(df_claims['claim_date'], errors='coerce')
df_claims['claim_date'].dtype

# %%
df_policies['start_date'].dt.strftime('%d-%m-%Y')
df_policies.head()

# %%
#Checando e tratando valores duplicados
df_policies.drop_duplicates(inplace=True)
df_claims.drop_duplicates(inplace=True)

'policy_id' in df_claims and 'policy_id' in df_policies

#Integração dos dados

df_merge = df_policies.merge(df_claims, on='policy_id', how='inner')

#Validação da integração
#%%
df_merge.shape
#%%
df_merge.isnull().sum()

#%%
df_merge['policy_id'].nunique() == df_claims['policy_id'].nunique()
#%%

len(df_merge) / len(df_claims) #taxa de junção - quanto mais próximo de 1(ou 100%) melhor

#%%
df_merge.groupby('policy_id')['claim_id'].count()

#%%
df_merge.head()
#%%

#Como eu criei um novo dataframe, perdeu a conversão do tipo da coluna anterior. Convertendo novamente

df_merge['start_date'] = pd.to_datetime(df_merge['start_date'], errors='coerce')
df_merge['end_date'] = pd.to_datetime(df_merge['end_date'], errors='coerce')
df_merge['claim_date'] = pd.to_datetime(df_merge['claim_date'], errors='coerce')
#%%

#Conversao das datas de YYYY-MM-DD para DD-MM-YYYY - converte do tipo datetime para um string, não podendo fazer novas operações

df_merge['start_date'] = df_merge['start_date'].dt.strftime('%d-%m-%Y')
df_merge['end_date'] = df_merge['end_date'].dt.strftime('%d-%m-%Y')
df_merge['claim_date'] = df_merge['claim_date'].dt.strftime('%d-%m-%Y')

#%%
df_merge.head()
#Exportação dos dados
#%%
df_merge.to_parquet("policy_claims.parquet", index=False)

# %%
