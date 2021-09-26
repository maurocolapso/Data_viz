from scipy.stats import spearmanr
from numpy.random import seed
from numpy.random import randn
import json
from numpy.core.fromnumeric import prod
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

with open('/Users/mauro/Documents/Data Visualization/Data_viz/Spotify/Data/StreamingHistory0.json', encoding='utf8') as f:
    data = json.load(f)

spotifiy_data = pd.DataFrame()


def extract_json_value(column_name):
    return[i[column_name] for i in data]


spotifiy_data['artist_name'] = extract_json_value('artistName')
spotifiy_data['end_time'] = extract_json_value('endTime')
spotifiy_data['ms_played'] = extract_json_value('msPlayed')
spotifiy_data['track_name'] = extract_json_value('trackName')

data_subset = spotifiy_data.sort_values(by=['ms_played'], ascending=False)

data = data_subset.groupby('track_name')['ms_played'].sum().reset_index()
data_sort = data.sort_values(by=['ms_played'], ascending=False)
data_sorter = data_sort.iloc[0:10, :]

sn.set_style('dark')
fig, ax = plt.subplots(tight_layout=True)

sn.barplot(x='ms_played', y='track_name', data=data_sorter)
fig.suptitle('Most played songs (Sep 2020 to Jan 2021)')
plt.show()
data_subset['end_time'].min()
data_subset['end_time'].max()


data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)
data3 = data2 + (10 * randn(1000) + 50)
data4 = data3 + (10 * randn(1000) + 50)
data5 = data4 + (10 * randn(1000) + 50)

# Similarity index

a = [data1, data2, data3, data4,data5]

spectra_correlations = []
for f in range(len(a)):  # go through each spectra
    print('scan #', f+1)
    correlation_temp = []
    # go through each spectra except current one
    for i in [x for x in range(len(a)) if x != f]:
        corr, _ = spearmanr(a[f], a[i])
        # appends all correlations of current spectra
        correlation_temp.append(corr)
    # calculate the product of the correlations of current spectra
    spectra_corr = np.prod(correlation_temp)
    print('similarity index = %.3f' % spectra_corr)
    spectra_correlations.append(spectra_corr)

# plot of smiliratoty index and number os scan
number_scans =  range(1,len(a)+1)
plt.plot(number_scans,spectra_correlations)
plt.show()

# plot of spectra1 vs spectra 2
plt.scatter(data1,data2)
plt.show()


T = np.array([1,2,3,4])
X = np.arange(8).reshape((2,4)) #spectras to be aling 
Seg = np.array([1,1])
nX,pX = X.shape # nX number of signals
                # pX number of data points
pT = T.size     # number of data points of target spectra
XWarped = np.zeros((nX, pT))

Seg = np.round(Seg)
Pre_Bound = len(Seg) > 1

Seg(:,1)
