###########   1 Package   ####################   
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pickle
from sas7bdat import SAS7BDAT
import scipy.io
from sqlalchemy import create_engine
from urllib.request import urlretrieve,urlopen, Request
import requests
from bs4 import BeautifulSoup
import tweepy
import time

######################   Twitter API    #########################


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="EQr5kHd5JhQrsOvAk7x5Ak2LU"
csecret="LisjBswI88wuW0OV6LUkIJZkEOYKm7vSzqsJQWMQfXc3eKXwIy"
atoken="790128816647614464-Pu6fOFne0TbgEgxPpZdu7xXAW9tBhed"
asecret="6dJI4x5xUY47AmIj6ueMNd77Sew7fYYZBG9MnVxZ9eUkQ"

class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return(True)
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

