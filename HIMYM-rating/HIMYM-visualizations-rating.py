import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_episodes_info.csv',index_col='season')
df_seasonvsepi = df[['episode_number','rating']]

df_wide = df_seasonvsepi.pivot(columns='episode_number', values='rating')

sns.set_style("white")
fig,ax=plt.subplots(figsize=(7,8))
sns.heatmap(df_wide.T,cmap="RdYlGn",linewidths=1,square=True)
fig.suptitle('HIMYM IMbd episodes rating ',ha='center',fontsize=24,fontweight='bold')
ax.set_xlabel('Season',fontsize=16,fontweight='bold')
ax.set_ylabel('Episode',fontsize=16,fontweight='bold')
plt.yticks(rotation=0) 
plt.annotate('Best rating: Slap Bet', xy=(2, 9), xytext=(-7, 9),
             arrowprops=dict(facecolor='green', shrink=0.05),
             )
plt.annotate('Worst rating: \nLast Forever: Part Two', xy=(9, 24), xytext=(10, 26),
             arrowprops=dict(facecolor='red', shrink=0.05),
             )
plt.show()
fig.savefig('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_rating.png',bbox_inches ='tight')

number_total = np.arange(0,208,1)
plt.stem(number_total[10],df['rating'])
plt.show()
plt.plot(number_total, df['rating'])
plt.show()

df['episode_number_total'] = number_total
df.set_index('episode_number_total',inplace=True)
column = df["rating"]
max_index = column.idxmax()
min_index = column.idxmin()
df.iloc[min_index]

df.iloc[min_index]
df.iloc[max_index]

df = pd.read_csv('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_episodes_info.csv')
mean_season_rating = df.groupby('season')['rating'].mean()
number_total = np.arange(1,209,1)
df['episode_number_total'] = number_total

first_season = df[df['season'] == 1]
second_season = df[df['season'] == 2]
plt.stem(first_season['episode_number_total'],first_season['rating'],bottom=mean_season_rating.iloc[0])
plt.stem(second_season['episode_number_total'],second_season['rating'],bottom=mean_season_rating.iloc[1])
plt.show()

seasons = np.arange(1,10,1)
fig,ax = plt.subplots()
ax.set_ylabel('Episode number')
ax.set_xlabel("Rating")

for season in seasons: 
    plt.stem(df[df['season'] == season]['episode_number_total'],df[df['season'] == season]['rating'],bottom=mean_season_rating.iloc[season-1])
plt.show()
