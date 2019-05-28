import tweepy
import os
import time

#Tokens and Keys for Login...

consumer_key_token = ""
consumer_secret_token = ""
access_token_token = ""
access_secret_token = ""

#login to twitter api
auth = tweepy.OAuthHandler(consumer_key_token, consumer_secret_token)
auth.set_access_token(access_token_token, access_secret_token)
api = tweepy.API(auth)

#Folder path where images reside
path = "" #Enter the images folder path here

os.chdir(path)

for image in os.listdir('.'):
    api.update_profile_image(image)
    time.sleep(3600) # In Seconds
