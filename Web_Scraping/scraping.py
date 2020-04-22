# Command: python scraping.py x y
# Scrapes x pages from website and shows news having points >= y

import requests
import pprint
import sys
from bs4 import BeautifulSoup

link_list = []
subtext_list = []
res = []

def get_data(max_page_number):
   for num in range(max_page_number):
      res.append(requests.get(f'https://news.ycombinator.com/news?p={num}'))
      soup = BeautifulSoup(res[num].text, 'html.parser')
      link = soup.select('.storylink')
      link_list.append(link)
      subtext = soup.select('.subtext')
      subtext_list.append(subtext)

get_data(int(sys.argv[1]))                                               # Number of pages to scrape
get_points = int(sys.argv[2])                                            # User Input Points

def sorted_news(items):                                                  # Sort news based on points
   return sorted(items, key = lambda k: k['votes'], reverse = True)

def custom_site(links, subtext):
   items = []

   for idx_1,item in enumerate(links):

      for idx_2, single_item in enumerate(item):
         title = single_item.getText()
         href = single_item.get('href', None)
         vote = subtext[idx_1][idx_2].select('.score')

         if len(vote):
            points = int(vote[0].getText().replace(' points', ''))

            if points >= get_points:                                          # Filter Points
               items.append({'title':title, 'link':href, 'votes': points})

   return sorted_news(items)
pprint.pprint(custom_site(link_list, subtext_list))



