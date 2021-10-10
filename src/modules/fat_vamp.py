import requests
import constants
import sys
from bs4 import BeautifulSoup
sys.path.append('..src')


def get_news(url):
    news = []
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if (response.status_code == 200):
        soup = BeautifulSoup(response.content, 'lxml')
        news_table = soup.find('table', id='news-table')
        # Limit in case we run into character length issues
        news_link = news_table.find_all('a', class_='tab-link-news', limit=2)

        for link in news_link:
            news.append({'link': link['href'], 'text': link.text})
    else:
        print(f'{response.status_code} received at {url}')
        news.append(constants.NO_NEWS)

    return news
