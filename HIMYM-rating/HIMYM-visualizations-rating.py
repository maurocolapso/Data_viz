import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_episodes_info.csv')
df_seasonvsepi = df[['episode_number','rating']]

df_wide = df_seasonvsepi.pivot(columns='episode_number', values='rating')

fig,ax=plt.subplots(figsize=(7,7))
sns.heatmap(df_wide.T,cmap="RdYlGn",linewidths=1,square=True)
plt.show()

number_total = np.arange(1,209,1)
plt.plot(number_total, df['rating'])
plt.show()

column = df["rating"]
max_index = column.idxmax()
min_index = column.idxmin()