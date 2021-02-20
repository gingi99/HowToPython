import os
import tweepy
from dotenv import load_dotenv

load_dotenv(verbose=True)
load_dotenv('.env')

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.get_user(screen_name = "@wankosobanyanko")
print(user.id)
print(user.name)
print(user.screen_name)
print(user.description)
print(user.statuses_count)
print(user.friends_count)
print(user.followers_count)
