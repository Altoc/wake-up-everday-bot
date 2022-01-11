import os
import time
import datetime
import tweepy
from dotenv import load_dotenv

#Authenticate Twitter Keys
dotenv_path = 'keys.env'
load_dotenv(dotenv_path)

c_key = os.getenv('CONSUMER_KEY')
c_sec = os.getenv('CONSUMER_SECRET')
a_tk = os.getenv('ACCESS_TOKEN_KEY')
a_ts = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(c_key, c_sec)
auth.set_access_token(a_tk, a_ts)
api = tweepy.API(auth, wait_on_rate_limit=True)

upload_result = api.media_upload('vid.mp4')
#if initial run, wait until next occurrance of 8am
now = datetime.datetime.today()
target = datetime.datetime(now.year, now.month, now.day, 8, 00)
if now.hour == target.hour:
    print("the time is now")
    #And now loop until heat death
    while 1:
        api.update_status(status="", media_ids=[upload_result.media_id_string])
        secondsInADay = 60 * 60 * 24
        time.sleep(secondsInADay)

