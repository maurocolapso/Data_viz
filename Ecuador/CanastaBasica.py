import matplotlib
from matplotlib.transforms import Transform
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from datetime import datetime

url = "/Users/mauro/Documents/Data Visualization/Data_viz/Ecuador/Data/202108_Tabulados_Mercado_Laboral_EXCEL.xlsx"
df = pd.read_excel(url, sheet_name=2,skiprows=2)
df.columns = ['Encuesta',"Periodo",'Indicadores','Total','Urbana','Rural',"Hombre",'Mujer']

df_desempleo = df[df['Indicadores'] == 'Desempleo (%)']
df_desempleo['Periodo'] = df_desempleo['Periodo'].str.capitalize()
df_desempleo['Periodo'] = pd.to_datetime(df_desempleo['Periodo'])
df_desempleo

fig,ax = plt.subplots()
ax.plot(df_desempleo['Periodo'],df_desempleo['Hombre'],'-o',label='Hombres')
ax.plot(df_desempleo['Periodo'],df_desempleo['Mujer'],'-o',label='Mujeres')
ax.set_title('Taza de desempleo en el Ecuador desde 2007 al 2021',loc='left')
plt.show()

rng = df_desempleo['Periodo']
x = datetime.strptime(rng, '%b-%y')
x
y = x.strftime('%b-%Y')
