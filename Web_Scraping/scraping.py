# Scrape news-data from Hacker News

import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')                            # Uses CSS Selector and returns list
links2 = soup2.select('.storylink') 

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

combined_links = links + links2
combined_subtext = subtext + subtext2

# print(links[0].getText())
# print(votes[0].get('id'))

def sorted_news(items):
   return sorted(items, key = lambda k: k['votes'], reverse = True)

def custom_site(links, subtext):
   items = []
   for idx, item in enumerate(links):

      title = item.getText()
      href = item.get('href', None)
      vote = subtext[idx].select('.score')
      if len(vote):
         points = int(vote[0].getText().replace(' points', ''))
         if points >= 100:
            items.append({'title':title, 'link':href, 'votes': points})

   return sorted_news(items)

pprint.pprint(custom_site(combined_links, combined_subtext))


