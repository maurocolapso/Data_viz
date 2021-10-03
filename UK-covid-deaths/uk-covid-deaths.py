import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import matplotlib.dates as mdates

df = pd.read_csv('UK-covid-deaths/Data/data_2021-Oct-03.csv')

fig,ax = plt.subplots()
sn.lineplot(x='date', y='cumDeaths28DaysByDeathDate',data=df,color='r',alpha=0.2)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=15))
ax.set_xlim('2020-03-02','2021-10-01')
ax.set_ylim(0,140000)
ax.fill_between(df['date'], df['cumDeaths28DaysByDeathDate'],color='r',alpha=0.2)
ax.yaxis.tick_right()

ax.vlines(x='2020-12-08',ymin=0,ymax=63833,color='r')

ax.text(0,1,'The Pace of Covid toll',fontweight='bold',fontsize=15,transform=ax.transAxes)
ax.text(0,0.8,'Deaths in the UK have steadied\nthanks to vaccination\n83% of adults are vaccinated',
        fontsize=12,transform=ax.transAxes)
plt.show()
