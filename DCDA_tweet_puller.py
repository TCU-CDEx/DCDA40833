# more on mining twitter at https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

# DO NOT SHARE THIS CODE WITH YOUR consumer key/secret and access token/secret included!!!! 

# before you can run this code, you may also need to install tweepy on your computer - you can do this by running "pip install tweepy" on the command line

# import modules
import tweepy
import json

# connect to Twitter API
# import submodule from tweepy module
from tweepy import OAuthHandler


# before you can run this code, you will need to log in to https://apps.twitter.com and create an "app" to get a consumer key, consumer secret, access token, and access secret
# define variables
consumer_key = "CONSUMER_KEY GOES HERE"
consumer_secret = "CONSUMER_SECRETE  GOES HERE"
access_token = "ACCESS_TOKEN GOES HERE"
access_secret = "ACCESS SECRET GOES HERE"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# continuously scrape tweets for a hashtag from the Twitter API and save to JSON file
# import submodule from tweepy module
from tweepy import Stream
from tweepy.streaming import StreamListener

# define variables
hashtag = "#YOUR Favorite Hashtag Here"
fname = hashtag + ".json"
 
# continuously scrape tweets and save to json file
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open(fname, 'a') as f:
                f.write(data)
                print("Another tweet was just captured! This is a never-ending process, use control-c to stop at any time.")
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=[hashtag])

