import json
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

with open ('/Users/mauro/Documents/Data Visualization/Data_viz/Spotify/Data/StreamingHistory0.json',encoding = 'utf8') as f:
    data = json.load(f)

spotifiy_data = pd.DataFrame()

def extract_json_value(column_name):
    return[i[column_name] for i in data]

spotifiy_data['artist_name'] = extract_json_value('artistName')
spotifiy_data['end_time'] = extract_json_value('endTime')
spotifiy_data['ms_played'] = extract_json_value('msPlayed')
spotifiy_data['track_name'] = extract_json_value('trackName')

data_subset = spotifiy_data.sort_values(by=['ms_played'],ascending=False)

data = data_subset.groupby('track_name')['ms_played'].sum().reset_index()
data_sort = data.sort_values(by=['ms_played'],ascending=False)
data_sorter = data_sort.iloc[0:10,:]

sn.set_style('dark')
fig,ax = plt.subplots(tight_layout=True)

sn.barplot(x='ms_played',y='track_name',data=data_sorter)
fig.suptitle('Most played songs (Sep 2020 to Jan 2021)')
plt.show()
data_subset['end_time'].min()
data_subset['end_time'].max()
