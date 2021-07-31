#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Importando bibliotecas

import os
import pandas as pd


# In[18]:


# Definindo diretório

os.chdir(r"D:\Documents\Scripts\TCC\Hits\Dataset\Bases Originais\Spotify")


# In[19]:


# Descreve número de registros e número de variáveis do dataset

def Descreve_Dataset(df):
    shape = df.shape
    print("O dataset apresenta " + str(shape[1]) + " variáveis (colunas) e " + str(shape[0]) + " registros.\n")
    
def Dataset_Colunas_Nulos(df):
    print("A seguir a listagem das colunas, seus tipos e seu nível de preenchimento:\n")
    
    display(df.columns)
    tab_info=pd.DataFrame(df.dtypes).T.rename(index={0:'Tipo'})
    tab_info=tab_info.append(pd.DataFrame(df.isnull().sum()).T.rename(index={0:'Nulos'}))
    tab_info=tab_info.append(pd.DataFrame(df.isnull().sum()/df.shape[0]*100).T.rename(index={0:'Nulos (%)'}))
    display(tab_info.transpose())
    
def Amostra_Dataset(df):
    print("Amostra para verificar o formato de preenchimento das colunas:\n")
    display(df.head().transpose())

analise_df = pd.read_csv('dataset-of-90s.csv')
Descreve_Dataset(analise_df)
Dataset_Colunas_Nulos(analise_df)
Amostra_Dataset(analise_df)

print ("A coluna artist apresenta "+ str(analise_df["artist"].unique().size) + " registros únicos.\n")


# In[20]:


# Descreve número de registros e número de variáveis do dataset

os.chdir(r"D:\Documents\Scripts\TCC\Hits\Dataset\Bases Originais\Lastfm")

analise_df = pd.read_csv('lastfm.csv')
Descreve_Dataset(analise_df)
Dataset_Colunas_Nulos(analise_df)
Amostra_Dataset(analise_df)

print ("A coluna artist_mb apresenta "+ str(analise_df["artist_mb"].unique().size) + " registros únicos.\n")

