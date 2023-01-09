# import packages
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# import data
uk_map = gpd.read_file(r'C:\Users\2166611p\OneDrive - University of Glasgow\Desktop\PhD\Scripts\JupyterNotebooks\GB_maps\Local_Authority_Districts__December_2017__Boundaries_in_Great_Britain.shp')
uk_map.head()

# import data cases data
url2 = "https://www.opendata.nhs.scot/dataset/b318bddf-a4dc-4262-971f-0ba329e09b87/resource/427f9a25-db22-4014-a3bc-893b68243055/download/trend_ca_20201012.csv"
df2 = pd.read_csv(url2)
df2.head()


# Extract date, council name, dailypositive and dailydeaths
df_council = df2[["CAName","DailyPositive",'DailyDeaths']].copy()

# Group by council name and sum cases
df_council_d = df_council.groupby(['CAName']).sum()

# extrac council names
x = df_council.CAName.unique()

# Select the rows with scotland council names
df_scotland = uk_map.iloc[326:358,:]
df_scotland.info()

# rename the lad17nm column to match CANname of covid-19 soctland data
df_scotland_council = df_scotland.rename(columns={'lad17nm':'CAName'})

# set index to the council names
df_scotland_council.set_index("CAName",inplace=True)

# rename the names of these two councils to macth one another, otherwise the merge will not work out
df_council_d.rename(index = {"Argyll & Bute":"Argyll and Bute",
                          "Dumfries & Galloway":"Dumbfries and Galloway",
                          "Perth & Kinross":"Perth and Kinross"},inplace=True)

# merge the two dataframes
result = pd.merge(df_scotland_council, df_council_d,left_index=True, right_index=True)

plt.rcParams['font.family'] = "DejaVu Sans" #set the font

# set a variable that will call with daily deaths to visualize on the map
VAL_DEATHS = 'DailyDeaths'

# set the range for the choropleth (number of deaths)
vmin, vmax = 0, 500

# create figure and axes for Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))

# create map
result.plot(column=VAL_DEATHS, cmap='PuBu', linewidth=0.8, ax=ax,edgecolor='0.8')
#edgecolor='0.8'

ax.axis('off')

# add a title
ax.set_title('Cumulative COVID-19 deaths in Scotland',fontsize=22,fontweight='bold',alpha=.75)

# Annotate the plot

ax.annotate('Source: Public Scotland, 2020',
           xy=(0.1, .08), xycoords='figure fraction',
           horizontalalignment='left', verticalalignment='top',
           fontsize=15, color='k')

ax.annotate('Mauro Pazmino',
           xy=(0.9, .08), xycoords='figure fraction',
           horizontalalignment='right', verticalalignment='top',
           fontsize=15, color='k')

# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='PuBu', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []

# size of colorbar
cbar = fig.colorbar(sm,shrink=0.4)

# Annotate where glasgow and edinburg are located
ax.annotate("Glasgow City",
            xy=(0.53, 0.175), xycoords='axes fraction',
            xytext=(0.3, 0.25), textcoords='axes fraction',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3"),
            )

ax.annotate("Edinburgh",
            xy=(0.68, 0.19), xycoords='axes fraction',
            xytext=(0.7, 0.25), textcoords='axes fraction',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3"),
            )

fig.text(0.15,0.145,'_____________________________________________________________________________________________________')
fig.savefig('../Covid-deaths-map-scotland/Scotland_maps.png', dpi = 300, bbox_inches ='tight')