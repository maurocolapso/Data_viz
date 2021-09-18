# import packages

import matplotlib.dates as mdates
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import seaborn as sns

# Import data daily cases from nhs scotlanld
url = "https://www.opendata.nhs.scot/dataset/b318bddf-a4dc-4262-971f-0ba329e09b87/resource/287fc645-4352-4477-9c8c-55bc054b7e76/download/daily_cuml_scot_20201012.csv"
df = pd.read_csv(url)
df.head()

# Transform column date into date data
df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d') 

# Calculate seven day mean 
df['Mean_7'] = df.iloc[:,1].rolling(window=7).mean()


# Plot

sns.set(font_scale=1.5) #set fontsize
sns.set_style("whitegrid") # set seaborn style
plt.rcParams['font.family'] = "DejaVu Sans" #BBC uses Helvetic font but matplotlib does not have it

fig, ax = plt.subplots(figsize=(9,7))


ax.plot(df["Date"],df["DailyCases"],color="orange",linewidth=2)
ax.plot(df["Date"],df["Mean_7"],color="purple",linewidth=2)
ax.plot(df.iloc[-1,0],df.iloc[-1,4],'s',color="purple")
ax.plot(df.iloc[-1,0],df.iloc[-1,1],'s',ms=4,color="orange") 

# asthetics of the plot

plt.grid(which='major', axis='x') # erase vertical lines of the grid
ax.xaxis.label.set_visible(False) # erase xlabel

# formating dates as day and month
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=8))
myFmt = mdates.DateFormatter('%d- %b')
ax.xaxis.set_major_formatter(myFmt)

# erase spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

#black line on x axis
plt.axhline(0,color="k",linewidth=2)

#ax.set_xlim('2020-8-10', '2020-10-14')
plt.show()

#ax.plot(df.iloc[228,0],df.iloc[228,4],'ro',color="darkcyan") #point
#ax.set_xlim('2020-8-10', '2020-10-14')