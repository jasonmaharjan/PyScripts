import tweepy
import time

consumer_key = '#'
consumer_secret = '#'

access_token = '#'
access_token_secret = '#'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


# API request-limit handler
def limit_handler(cursor):
   try:
      while True:
         yield cursor.next()                 

   except tweepy.RateLimitError:
      time.sleep(1000)


# Follow-Back Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
   try:
      if follower.followers_count < 100:
         follower.follow()
         print(f'{follower.name} followed!')

   except StopIteration:
      break


# Like-Retweet Bot
search_keyword = 'python', 'AI'
no_of_tweets = 10 

for tweet in limit_handler(tweepy.Cursor(api.search, search_keyword).items(no_of_tweets)):
   try:
      tweet.favorite()
      tweet.retweet()
      print('Favourite')

   except tweepy.TweepError as error:
      print(error.reason)

   except StopIteration:
      break

