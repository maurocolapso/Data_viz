from requests import get
from bs4 import BeautifulSoup
import pandas as pd

himym_episodes = []

for season in range(1, 10):
    response = get(
        'https://www.imdb.com/title/tt0460649/episodes?season=' + str(season))
    page_html = BeautifulSoup(response.text, 'html.parser')
    episode_containers = page_html.find_all('div', class_='info')

    for episodes in episode_containers:
        season = season
        episode_number = episodes.meta['content']
        title = episodes.a['title']
        airdate = episodes.find('div', class_='airdate').text.strip()
        rating = episodes.find('span', class_='ipl-rating-star__rating').text
        total_votes = episodes.find(
            'span', class_='ipl-rating-star__total-votes').text
        desc = episodes.find('div', class_='item_description').text.strip()

        episode_data = [season, episode_number,
                        title, airdate, rating, total_votes, desc]

        himym_episodes.append(episode_data)

HIMYM_episodes = pd.DataFrame(himym_episodes, columns=[
                              'season', 'episode_number', 'title', 'airdate', 'rating', 'total_votes', 'desc'])
HIMYM_episodes.head()

# Clean data


def remove_str(votes):
    for r in ((',', ''), ('(', ''), (')', '')):
        votes = votes.replace(*r)

    return votes


HIMYM_episodes['total_votes'] = HIMYM_episodes.total_votes.apply(
    remove_str).astype(int)
HIMYM_episodes.head()

HIMYM_episodes['rating'] = HIMYM_episodes.rating.astype(float)
HIMYM_episodes['airdate'] = pd.to_datetime(HIMYM_episodes.airdate)
HIMYM_episodes.info()

# export clean data

HIMYM_episodes.to_csv(
    '/Users/mauro/Documents/Data Visualization/Data_viz/HIMYM-rating/HIMYM_episodes_info.csv', index=False)
