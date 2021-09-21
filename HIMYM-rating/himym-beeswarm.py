import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_episodes_info.csv')
df_season_episode = df[['season','episode_number','rating']]
df_season_episode = df_season_episode.copy() 
df_season_episode["season"] = df_season_episode["season"].astype(str)

fig,ax=plt.subplots(figsize=(8,8))
sns.set(style='white')
sns.swarmplot(x="rating",y='season',data=df_season_episode,size=6,ax=ax)
ax.set_xlable('IMDb rating')
ax.set_ylabel('Seasons')
fig.text(0, 0.95, "How I Met Your Mother", fontsize=25, fontweight='bold',transform=fig.transFigure)
fig.text(0, 0.9, "IMDb rating per episode", fontsize=18, color='gray',transform=fig.transFigure)

plt.grid()
plt.show()