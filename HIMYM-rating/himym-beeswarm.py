import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_episodes_info.csv')
df_season_episode = df[['season','episode_number','rating']]
df_season_episode = df_season_episode.copy() 
df_season_episode["season"] = df_season_episode["season"].astype(str)

fig,ax=plt.subplots(figsize=(12,7))
sns.set(style='white')
sns.swarmplot(x="rating",y='season',data=df_season_episode,size=6,ax=ax)
ax.set(ylabel='Seasons', xlabel='IMDb rating')
fig.text(0, 0.95, "How I Met Your Mother", fontsize=25, fontweight='bold',transform=fig.transFigure)
fig.text(0, 0.9, "IMDb rating per episode", fontsize=18, color='gray',transform=fig.transFigure)
plt.annotate('The Final Page: Part Two', xy=(9.5, 8), xytext=(10, 8.5),
             arrowprops=dict(facecolor='k', connectionstyle="angle3"),
             )
plt.annotate('Tick Tick Tick', xy=(9.5, 7), xytext=(10, 6.5),
             arrowprops=dict(facecolor='k', connectionstyle="angle3"),
             )
plt.grid()
#plt.show()
fig.savefig('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_beeswarm.png',bbox_inches ='tight')


#df_season_episode[df_season_episode['season'] == '7']


#df.iloc[171]
#df.iloc[145]