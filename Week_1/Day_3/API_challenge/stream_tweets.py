import twitter
import os
from IPython.display import JSON
import json
import requests as re

consumer_key = os.environ["TW_CONSUMER_KEY"]
consumer_secret = os.environ["TW_CONSUMER_SECRET"]
access_token = os.environ["TW_ACCESS_TKN"]
access_token_secret = os.environ["TW_ACCESS_TKN_SECRET"]

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


## FOLLOWING FUNCTION WILL COLLECT REAL-TIME TWEETS IN OUR COMPUTER

# data returned will be for any tweet mentioning strings in the list FILTER
FILTER = ['#datascience', ":)"]

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
LANGUAGES = ['en']

SAVEFILE = '/home/ishnu/bootcamp/stream_tweets_output.txt'

def main():
    count = 0
    with open(SAVEFILE, 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        for line in api.GetStreamFilter(track=FILTER, languages=LANGUAGES):
            f.write(json.dumps(line))
            f.write('\n')
            count += 1
            if count >500:
                break
            
main()