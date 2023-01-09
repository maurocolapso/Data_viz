from statsbombpy import sb
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch

# Get data from statsbobpy
comp = sb.competitions()

# get a specific match
match = 3775610
match_events = sb.events(match_id=match)
match_events.to_csv('events.csv', index=False)

# seperate location into x and y components for scatterplot
match_events[['location_x', 'location_y']] = match_events['location'].apply(pd.Series)

# Select columns and clean NA values
data_clean = match_events[['team', 'location_x', 'location_y', 'shot_statsbomb_xg', 'shot_outcome']].copy()
data_clean = data_clean.dropna()


# filter data by team and then by shot outcome
bristol_city = data_clean[data_clean.team == 'Bristol City WFC']
manchester_united = data_clean[data_clean.team == 'Manchester United']

bristol_city_goal = bristol_city[bristol_city.shot_outcome == 'Goal']
bristol_city_off_t = bristol_city[bristol_city.shot_outcome == 'Off T']
bristol_city_blocked = bristol_city[bristol_city.shot_outcome == 'Blocked']
bristol_city_saved = bristol_city[bristol_city.shot_outcome == 'Saved']

manchester_goal = manchester_united[ manchester_united.shot_outcome == 'Goal']
manchester_off_t = manchester_united[ manchester_united.shot_outcome == 'Off T']
manchester_blocked = manchester_united[ manchester_united.shot_outcome == 'Blocked']
manchester_saved = manchester_united[ manchester_united.shot_outcome == 'Saved']


number = 1000

# Picth format
pitch = Pitch(line_color='#6594C0', pitch_color='#011021', linewidth=0.7)


# Scatterplots on each pitch
fig, ((ax1, ax2), (ax3, ax4)) = pitch.draw(nrows=2,ncols=2, figsize=(10,8))

pitch.scatter(manchester_blocked.location_x, manchester_blocked.location_y, ax=ax1, s=manchester_blocked.shot_statsbomb_xg*number, c='red')

pitch.scatter(120 - bristol_city_blocked.location_x, bristol_city_blocked.location_y, ax=ax1, s=bristol_city_blocked.shot_statsbomb_xg*number, c='white')


pitch.scatter(manchester_goal.location_x, manchester_goal.location_y, ax=ax2, s=manchester_goal.shot_statsbomb_xg*number, color='red')
pitch.scatter(120 - bristol_city_goal.location_x, bristol_city_goal.location_y, ax=ax2, s=bristol_city_goal.shot_statsbomb_xg*number, color='white')


pitch.scatter(manchester_off_t.location_x, manchester_off_t.location_y, ax=ax3, s=manchester_off_t.shot_statsbomb_xg*number, color='red')
pitch.scatter(120 - bristol_city_off_t.location_x, bristol_city_off_t.location_y, ax=ax3, s=bristol_city_off_t.shot_statsbomb_xg*number, color='white')


pitch.scatter(manchester_saved.location_x, manchester_saved.location_y, ax=ax4, s=manchester_saved.shot_statsbomb_xg*number, color='red')
pitch.scatter(120 - bristol_city_saved.location_x, bristol_city_saved.location_y, ax=ax4, s=bristol_city_saved.shot_statsbomb_xg*number, color='white')

# Text and formatting
axes = [ax1, ax2, ax3, ax4]
labels = ['Blocked', 'Goal', 'Off Target', 'Saved']
for ax, label in zip(axes, labels):
    ax.set_title(label, weight='bold', color='white')
fig.set_facecolor(color='#011021')


fig.text(0.5, 0, "Data Source: StatsBomb", color= 'white', fontsize=7, ha='center')

fig.text(0.5, 1.2, "Bristol city", color='white',fontsize=20, weight='bold', ha='right')

fig.text(0.5, 1.15, 'vs', color='#6594C0', fontsize=20, weight='bold', ha='center')

fig.text(0.5, 1.1, "Manchester United", fontsize=20, weight='bold', color='red', ha='left')

fig.text(0.5, 1.05, "Shots maps by shot outcome | England - FA Women's Super League Regular Season 2021", ha='center', fontsize=7, color = '#6594C0')

fig.text(0.5, 1.02, "The white circles represent Bristol City and the red circles repsent Manchester United. The sizes of the circles represent the probabillity of a shot resulting in a goal", ha='center', fontsize=7, color='#6594C0')

fig.text(1, 0, "@chinito_colapso", color= 'white', fontsize=7, ha='right')

fig.savefig('Football.png', dpi=300, bbox_inches='tight')