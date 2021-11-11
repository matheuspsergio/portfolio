
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import glob
import datetime
from datetime import datetime, date, timedelta

#carregando o df com tipo de petrecho por mmsi
df_apoio = pd.read_csv('file_path/fishing_vessels_v20190520_fishing_vessels_v20190702.csv')

#convertendo formato do mmsi para numero
df_apoio['mmsi'] = df_apoio['mmsi'].astype(np.int32)

#carregando o arquivo de referência para as analises gfw_real
ref = pd.read_csv('file_path/lista_arcgis.csv')

#A pasta está localizado os dados que eu usei
file_path = 'file_path/daily_csv'

#Nesse trecho de código, todos os arquivos localizados na pasta de cima, são juntados em um único arquivo
read_files = glob.glob(os.path.join(file_path, '*.csv'))

np_array_values = []

for files in read_files:
    dia_naveg = pd.read_csv(files, header=0)
    np_array_values.append(dia_naveg)

frame = pd.concat(np_array_values, axis = 0, ignore_index = True)


# In[ ]:


#filtrar dados proximos ao brasil
#lat e lon se referem a latitude e longitude, respectivamente
df = frame.query('( -500 <= lat_bin <= 140) & (-700 <= lon_bin <= -180)').copy()

#dividr os valores das coordenadas pra ficar em graus
df['lat_bin'] = df['lat_bin']/10
df['lon_bin'] = df['lon_bin']/10

#adicionando geartype de cada embarcação VER NOTA DE RODA PÉ
df = df.merge(df_apoio, on='mmsi', sort=False )

#colocar date no formato datetime
df['date'] = pd.to_datetime(df['date'])

#sort by date
df.sort_values(['mmsi', 'date'], ascending=[True, False])

#colocar previous latitude e longitude - O objetivo era criar 'strings' de atividade pesqueira consecutiva, que fornarian os
#cruzeiros de pesca

#essa prineira linha tem apenas as condições: se o time delta for menor que 6 dias e o mmsi for igual à linha anterior
df['lat_prev'] = np.where((df['date'] - df['date'].shift(1) < timedelta(days= 6)) & (df['mmsi'] == df['mmsi'].shift(1)),
                          df['lat_bin'].shift(1), df['lat_bin']) #o que faz tá aqui, sendo true e false separados por vírgulas


df['lon_prev'] = np.where((df['date'] - df['date'].shift(1) < timedelta(days= 6)) & (df['mmsi'] == df['mmsi'].shift(1)),
                          df['lon_bin'].shift(1), df['lon_bin'])        


# In[ ]:


#O que precisa pro gfw_estimado (não teve a validação dos dados no RGP- o momento em que o df2 é criado na célula de baixo)

#criar colunas de month e week
df['week'] = df['date'].dt.week
df['month'] = df['date'].dt.month

#salvando todos os anos - para acompanhar o crescimento da frota dentro da GFW
df.to_csv('file_path/gfw_est_all_years.csv', index= False)

#Máscara com apenas o ano de 2018, que foi o foco de minhas análises
df = df[df['date'].dt.year == 2018]

#salvando só 2018
df.to_csv('file_path/gfw_est_all_years.csv', index= False)


# In[ ]:


#O que precisa pro gfw_real- embarcações que de fato foram validadas pelo RGP

#limitar para as embarcações presentes no rgp
df2 = df.query('mmsi in @ref.mmsi').copy()

#colocar os dados reais obtidos pelo rgp
df2 = df2.merge(ref[['mmsi','petrecho', 'Comprimento', 'AB']], on='mmsi')

#salvando
df2.to_csv('file_path/gfw_real.csv', index= False, encoding='latin-1')


# In[30]:


#Apenas testando se o merge foi feito corretamente
testing = frame.query('mmsi in @ref.mmsi').copy()

testing.mmsi.unique()


# Após ter começado a estudar bases de dados relacionais, vejo que não procedi da melhor forma no df.merge da célula 2. Na prática, eu adicionei muito dado desnecessário ao meu arquivo. Hoje em dia, eu teria feito o merge somente no momento da consulta que eu precisei fazer, e não teria mantido os dados juntos tal como eu acabei fazendo
