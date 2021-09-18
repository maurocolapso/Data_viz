import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import bar_chart_race as bcr

df = pd.read_csv(
    "/Users/mauro/Documents/Data Visualization/Data_viz/bar-race-max-min-temp-Glasgow/paisleydata_mod.csv")
df['yyyy'] = pd.to_datetime(df.yyyy, format='%Y')
df['mm'] = df['mm'].replace([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [
                            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', "Dec"])
df['tmax'] = df['tmax'].str.replace('*', '', regex=True)
df['tmin'] = df['tmin'].str.replace('*', '', regex=True)

df[['tmax', 'tmin']] = df[['tmax', 'tmin']].apply(pd.to_numeric)
df_tmax_peryear = df.groupby('yyyy')['tmax'].mean().reset_index()
df_tmin_peryear = df.groupby('yyyy')['tmin'].mean().reset_index()

df_long = df.pivot(index=["yyyy"], columns='mm', values='tmax').reset_index()
df_long.fillna(0.0, inplace=True)
df_long.set_index('yyyy')

df_long.to_csv("weather.csv")


df = pd.read_csv(
    "/Users/mauro/Documents/Data Visualization/Data_viz/weather.csv", index_col='yyyy')


fig, ax = plt.subplots(figsize=(7, 10), tight_layout=True)
plt.rcParams.update({'font.size': 22})
fig.suptitle('Maximun Temperatures in Glasgow (1959-2021)',
             fontsize=16, fontweight='bold')
ax.set_title('Maximum monthly temperature in celsius ')
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)
ax.spines.left.set_visible(False)
plt.yticks(fontsize=14)

plt.tick_params(axis='x', which='both', bottom=False,
                top=False, labelbottom=False)

bcr.bar_chart_race(df=df, filename='bar.mp4', cmap='gnuplot', fig=fig,
                   bar_label_size=14, steps_per_period=20, period_length=500)


fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(df_tmax_peryear.iloc[:, 0], df_tmax_peryear.iloc[:, 1], color='red')
ax.set_title(
    'Mean Maximun Temperatures in Glasgow (Pasley Station) from 1959 to 2021')
ax.set_xlabel('Years')
ax.set_ylabel('Mean Maximun temperature (C)')
plt.show()

df_1959 = df[df['yyyy'] == '1959-01-01']
df_1959_copy = df_1959.copy()
df_1959_copy['mm'] = df_1959_copy['mm'].replace([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [
                                                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', "Dec"])

df_1959_copy
plt.barh(df_1959_copy['mm'], df_1959_copy['tmax'])
plt.show()

plt.plot(df_tmin_peryear.iloc[:, 0], df_tmin_peryear.iloc[:, 1])
plt.show()
