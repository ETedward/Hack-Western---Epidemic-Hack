import tweepy
from tweepy import OAuthHandler

consumer_key = '3G76QGYdsSgV408kqHRQjsVB5'
consumer_secret = 'KiH4PPSILrk0C5kpzQa9PUPvjQiRX4LZfZjOqMHXYXc5EvtkgO'
access_token = 	'4541083965-g8ww8TXzSeyLixNruo0h8UnC8ruqrRecQue43Ph'
access_secret = 'XcGqtH9QynD7a8PdM0M75cAcjlRilHbljmfkR8sLyiL1P'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
import json
#import geojson

"""
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
    print "-----------"
"""

with open('python.json', 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        print (type(tweet))
        print ("hey")
        #if tweet.get('coordinates', None) is not None:
        if 'coordinates' in tweet:            
            print("hello")
            print(type(tweet['coordinates']))
            print(type(tweet))
            geo_json_feature = {
                "type": "Feature",
                 "geometry": tweet['coordinates'],
                
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                    
                    }
                }
            geo_data['features'].append(geo_json_feature)
            #print(str(geo_json.feature))
     
# Save geo data
with open('geo_data.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))
