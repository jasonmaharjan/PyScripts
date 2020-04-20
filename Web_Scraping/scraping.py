# Command: python scraping.py x y
# Scrapes x pages from website and shows news having points >= y

import requests
import pprint
import sys
from bs4 import BeautifulSoup

link_list = []
subtext_list = []

def get_data(max_page_number):
   for num in range(max_page_number):
      res = requests.get(f'https://news.ycombinator.com/news?p={num}')
      soup = BeautifulSoup(res.text, 'html.parser')
      link = soup.select('.storylink')
      link_list.append(link)
      subtext = soup.select('.subtext')
      subtext_list.append(subtext)
   
get_data(int(sys.argv[1]))                      # Number of pages to scrape(User Input)
get_points = int(sys.argv[2])                   # User Input Points

combined_links = link_list[0]
combined_subtext = subtext_list[0]

def sorted_news(items):                         # Descending Order of points
   return sorted(items, key = lambda k: k['votes'], reverse = True)

def custom_site(links, subtext):
   items = []
   for idx, item in enumerate(links):

      title = item.getText()
      href = item.get('href', None)
      vote = subtext[idx].select('.score')
      if len(vote):
         points = int(vote[0].getText().replace(' points', ''))
         if points >= get_points:                # Filter Points
            items.append({'title':title, 'link':href, 'votes': points})

   return sorted_news(items)

pprint.pprint(custom_site(combined_links, combined_subtext))


