import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.transforms import Transform

url = "/Users/mauro/Documents/Data Visualization/Data_viz/Ecuador/Data/202108_Tabulados_Mercado_Laboral_EXCEL.xlsx"
df = pd.read_excel(url, sheet_name=2, skiprows=2)
df.columns = ['Encuesta', "Periodo", 'Indicadores',
    'Total', 'Urbana', 'Rural', "Hombre", 'Mujer']

df_desempleo = df[df['Indicadores'] == 'Desempleo (%)']
df_desempleo_copy = df_desempleo.copy()

# change dates into proper format (making sure momnths are in english)
df_desempleo_copy['Periodo'] = df_desempleo_copy["Periodo"].str.capitalize()
df_desempleo_copy['Periodo'] = '01-' + df_desempleo_copy['Periodo'].astype(str)
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace(
    'Dic', 'Dec')
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace(
    'Ago', 'Aug')
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace(
    'Abr', 'Apr')
df_desempleo_copy['Periodo'] = df_desempleo_copy['Periodo'].str.replace(
    'Ene', 'Jan')


df_desempleo_copy['Periodo'] = pd.to_datetime(df_desempleo_copy['Periodo'])

# Plot
mujeres = '#1d70b8'
dark_mujeres = '#003078'
hombres = 'gray'
background_color = "#fafafa"


fig, ax = plt.subplots(figsize=(10, 5), facecolor=background_color)
ax.plot(df_desempleo_copy['Periodo'], df_desempleo_copy['Hombre'],
        '-o', label='Hombres', color=hombres)
ax.plot(df_desempleo_copy['Periodo'], df_desempleo_copy['Mujer'],
        '-o', label='Mujeres', color=mujeres)
ax.set_ylim(0,10)
ax.set_facecolor(background_color)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#ax.axvspan(datetime(2007,1,15), datetime(2017,5,24),alpha=0.5, color='red')
#ax.axvspan(datetime(2017,5,24), datetime(2021,5,24),alpha=0.5, color='green')
#plt.show()

ax.text(0, 1.1, 'Taza de desempleo en el Ecuador desde 2007 al 2021',
        fontweight='bold', fontfamily='arial', fontsize=20,
        ha='left', va='bottom', transform = ax.transAxes)
ax.text(0, 1.05, 'La disparidad de las tazas de desemplo en hombres y mujeres a travez de los años',
        fontfamily='arial', fontsize=15,
        ha='left', va='bottom', color='gray',transform = ax.transAxes)
ax.text(1, 0.4, 'Hombres', fontfamily='arial', fontsize=15, fontweight='bold',
        ha='left', va='bottom', color=hombres,transform = ax.transAxes)
ax.text(1, 0.6, 'Mujeres', fontfamily='arial', fontsize=15, fontweight='bold',
        ha='left', va='bottom', color=mujeres,transform = ax.transAxes)
fig.savefig('/Users/mauro/Documents/Data Visualization/Data_viz/Ecuador/Unemployment_rate.png',bbox_inches ='tight')    
plt.show()









rng=df_desempleo_copy.iloc[0, 1]
x=datetime.strptime(rng, '%d-%b-%y')
x
y=x.strftime('%b-%Y')

df_desempleo_copy["Preiodo"]=df_desempleo_copy["Periodo"].apply(date.time(str))
new_dates=[]
for index, row, in df_desempleo_copy.iterrows():
    x=datetime.strptime(row["Periodo"], '%d-%b-%y')
    new_dates.append(x)
