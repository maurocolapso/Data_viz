import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.transforms import Transform

url = "/Users/mauro/Documents/Data Visualization/Data_viz/Ecuador/Data/202108_Tabulados_Mercado_Laboral_EXCEL.xlsx"
df = pd.read_excel(url, sheet_name=2,skiprows=2)
df.columns = ['Encuesta',"Periodo",'Indicadores','Total','Urbana','Rural',"Hombre",'Mujer']

df_desempleo = df[df['Indicadores'] == 'Desempleo (%)']
df_desempleo_copy = df_desempleo.copy()

# change dates into proper format (making sure momnths are in english)
df_desempleo_copy['Periodo'] = df_desempleo_copy["Periodo"].str.capitalize()
df_desempleo_copy['Periodo'] = '01-' + df_desempleo_copy['Periodo'].astype(str)
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace('Dic','Dec')
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace('Ago','Aug')
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace('Abr','Apr')
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace('Ene','Jan')


df_desempleo_copy['Periodo'] = pd.to_datetime(df_desempleo_copy['Periodo'])

# Plot
fig,ax = plt.subplots()
ax.plot(df_desempleo_copy['Periodo'],df_desempleo_copy['Hombre'],'-o',label='Hombres')
ax.plot(df_desempleo_copy['Periodo'],df_desempleo_copy['Mujer'],'-o',label='Mujeres')
ax.set_title('Taza de desempleo en el Ecuador desde 2007 al 2021',loc='left')
plt.show()









rng = df_desempleo_copy.iloc[0,1]
x = datetime.strptime(rng, '%d-%b-%y')
x
y = x.strftime('%b-%Y')

df_desempleo_copy["Preiodo"] = df_desempleo_copy["Periodo"].apply(date.time(str))
new_dates = []
for index, row, in df_desempleo_copy.iterrows():
    x = datetime.strptime(row["Periodo"], '%d-%b-%y')
    new_dates.append(x)