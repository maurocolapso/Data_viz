import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    "/Users/mauro/Documents/Data Visualization/Data_viz/bar-race-max-min-temp-Glasgow/paisleydata_mod.csv")
df['yyyy'] = pd.to_datetime(df.yyyy, format='%Y')

df['tmax'] = df['tmax'].str.replace('*', '', regex=True)
df['tmin'] = df['tmin'].str.replace('*', '', regex=True)

df[['tmax', 'tmin']] = df[['tmax', 'tmin']].apply(pd.to_numeric)
df_tmax_peryear = df.groupby('yyyy')['tmax'].mean().reset_index()
df_tmin_peryear = df.groupby('yyyy')['tmin'].mean().reset_index()

fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(df_tmax_peryear.iloc[:, 0], df_tmax_peryear.iloc[:, 1], color='red')
ax.set_title(
    'Mean Maximun Temperatures in Glasgow (Pasley Station) from 1959 to 2021')
ax.set_xlabel('Years')
ax.set_ylabel('Mean Maximun temperature (C)')
plt.show()

df_1959 = df[df['yyyy'] == '1959-01-01']
df_1959_copy = df_1959.copy()
df_1959_copy['mm'] = df_1959_copy['mm'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov',"Dec"])

df_1959_copy
plt.barh(df_1959_copy['mm'],df_1959_copy['tmax'])
plt.show()

plt.plot(df_tmin_peryear.iloc[:, 0], df_tmin_peryear.iloc[:, 1])
plt.show()
