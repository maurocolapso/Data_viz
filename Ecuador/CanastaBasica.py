import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.transforms import Transform

# unemployment
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



# trends between formal and informal labour
url = "/Users/mauro/Documents/Data Visualization/Data_viz/Ecuador/Data/202108_Tabulados_Mercado_Laboral_EXCEL.xlsx"
df_2 = pd.read_excel(url, sheet_name=3, skiprows=1)
df_2.head()

dates = df_desempleo_copy["Periodo"].reset_index(drop=True)
x = df_2.iloc[21:23,1:].T.reset_index(drop=True)
x.columns = ['Sector Formal',"Sector Informal"]
x = x.drop(0,axis=0)
x = x.reset_index(drop=True)
x["Periodo"] = dates
x = x.set_index('Periodo')
x = x*100

colors = ['#1d70b8','gray']
fig,ax = plt.subplots(figsize=(8,5),facecolor=background_color)
sn.lineplot(data=x,legend=False,palette=colors)
sn.despine()
ax.axvline(datetime(2017,5,24),color='k',ls='--')
ax.axvline(datetime(2021,5,24),color='k',ls='--')
ax.set_facecolor(background_color)

ax.text(0.15, 0.1, 'Sector Informal', fontfamily='arial', fontsize=15, fontweight='bold',
        ha='left', va='bottom', color=hombres,transform = ax.transAxes)
ax.text(0.15, 0.7, 'Sector Formal', fontfamily='arial', fontsize=15, fontweight='bold',
        ha='left', va='bottom', color=mujeres,transform = ax.transAxes)
ax.text(0, 1.05, 'Caracterizacion del Empleo en el Ecuador', fontfamily='arial', fontsize=20, fontweight='bold',
        ha='left', va='bottom',transform = ax.transAxes)
ax.text(0, 1, 'Porcentaje de Empleo formal e informal desde 2007 hasta 2021', fontfamily='arial', fontsize=15, fontweight='bold',
        ha='left', va='bottom',color='gray',transform = ax.transAxes)

#ax.text(0.2, 0.9, 'Presidencia: R. Correa', fontfamily='arial', fontsize=10, fontweight='bold',
#        ha='left', va='bottom',transform = ax.transAxes)
#ax.text(0.7, 0.9, 'Presidencia: L. Moreno', fontfamily='arial', fontsize=10, fontweight='bold',
#        ha='left', va='bottom',transform = ax.transAxes)
fig.savefig('/Users/mauro/Documents/Data Visualization/Data_viz/Ecuador/Formal_Informal.png',bbox_inches ='tight')  
plt.show()


df.columns = ['Encuesta', "Periodo", 'Indicadores',
    'Total', 'Urbana', 'Rural', "Hombre", 'Mujer']

np.random.seed(23)
observations = 75
df=pd.DataFrame(dict(A=np.random.uniform(low=-1, high=1.1, size=observations).tolist(),
                    B=np.random.uniform(low=-1, high=1.1, size=observations).tolist(),
                    C=np.random.uniform(low=-1, high=1.1, size=observations).tolist(),
                    ))
df.iloc[0,] = 0
df = df.cumsum()

firstdate = datetime(2020,1,1)
df['date'] = pd.date_range(firstdate, periods=df.shape[0]).tolist()
df.set_index('date', inplace=True)



rng=df_desempleo_copy.iloc[0, 1]
x=datetime.strptime(rng, '%d-%b-%y')
x
y=x.strftime('%b-%Y')

df_desempleo_copy["Preiodo"]=df_desempleo_copy["Periodo"].apply(date.time(str))
new_dates=[]
for index, row, in df_desempleo_copy.iterrows():
    x=datetime.strptime(row["Periodo"], '%d-%b-%y')
    new_dates.append(x)
