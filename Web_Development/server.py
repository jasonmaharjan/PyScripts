import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request
app = Flask(__name__)         # __name__ is set to __main__

# create 'templates' folder for html and 'static' folder for css and js
@app.route('/')
def render():
   return render_template('index.html')

@app.route('/<query>')
def test(query = None):
   return render_template('index.html', test = query)

@app.route('/results', methods = ['POST', 'GET'])
def display_results():
   if request.method == 'POST':
      data = request.form['pages']
      try:

         # Web Scraper
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

         get_data(int(data))                                          # Number of pages to scrape
         get_points = 10                                              # User Input Points

         def sorted_news(items):                                      # Sort News based on points         
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
         web_scraper_results = custom_site(link_list, subtext_list)
      
      except ValueError:
         web_scraper_results = 'No results were found!'

   return render_template('result.html', result = web_scraper_results)