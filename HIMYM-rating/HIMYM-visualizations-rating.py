import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_episodes_info.csv',index_col='season')
df_seasonvsepi = df[['episode_number','rating']]

df_wide = df_seasonvsepi.pivot(columns='episode_number', values='rating')

sns.set_style("white")
fig,ax=plt.subplots(figsize=(15,7), tight_layout=True)
sns.heatmap(df_wide.T,cmap="RdYlGn",linewidths=1)
#fig.suptitle('How I Met Your Mother',ha='center',fontsize=24,fontweight='bold')
ax.set_xlabel('Season',fontsize=16,fontweight='bold')
ax.set_ylabel('Episode',fontsize=16,fontweight='bold')
plt.yticks(rotation=0) 
plt.annotate('Highest rating: \nSlap Bet', xy=(1.5, 8.9), xytext=(-1.5, 9),
             arrowprops=dict(facecolor='green', shrink=0.05),
             )
plt.annotate('Highest rating: \nHow Your Mother Met Me', xy=(9, 16), xytext=(10, 20),
             arrowprops=dict(facecolor='green', shrink=0.05),
             )
plt.annotate('Lowest rating: \nLast Forever: Part Two', xy=(9, 24), xytext=(10, 26),
             arrowprops=dict(facecolor='red', shrink=0.05),
             )

plt.annotate('My personal favorite: \nThe Time Travelers', xy=(7.8, 19), xytext=(7.8, 27),
             arrowprops=dict(facecolor='k', shrink=0.05),
             )
             
ax.text(0, -3, "How I Met Your Mother", fontsize=25, fontweight='bold',transform=ax.transData)
ax.text(0, -1, "IMDb rating per episode", fontsize=18, color='gray',transform=ax.transData)
ax.text(0, 27, "Data Visualization: Mauro Pazmino/Data: IMDb", fontsize=12, color='gray',transform=ax.transData)
#plt.show()
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

color=['#d1d1d1','k']
first_season = df[df['season'] == 1]
second_season = df[df['season'] == 2]
plt.stem(first_season['episode_number_total'],first_season['rating'],
         color[0],bottom=mean_season_rating.iloc[0],basefmt=color[0],markerfmt='blueo')
plt.stem(second_season['episode_number_total'],second_season['rating'],
         color[1],bottom=mean_season_rating.iloc[1],basefmt=color[1],markerfmt=color[1])
plt.show()

plt.hlines()


seasons = np.arange(1,10,1)
fig,ax = plt.subplots()
ax.set_ylabel('Episode number')
ax.set_xlabel("Rating")#mmm

for season in seasons: 
    plt.stem(df[df['season'] == season]['episode_number_total'],df[df['season'] == season]['rating'],
             bottom=mean_season_rating.iloc[season-1])
plt.show()

plt.hlines(y=mean_season_rating.iloc[0],xmin=1,xmax=22) #first and last episode
plt.vlines(x=1,ymin=mean_season_rating.iloc[0],ymax=10) #rating
plt.vlines(x=2,ymin=mean_season_rating.iloc[0],ymax=7)

#plt.hlines(y=mean_season_rating.iloc[1],xmin=24,xmax=40)

plt.show()

#color = cm.rainbow(np.linspace(0, 1, n))
#for i, c in zip(range(n), color):
#   plt.plot(x, y, c=c)

count_episodes = df.groupby('season')['episode_number'].count()