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
import praw

#https://www.youtube.com/watch?v=KX2jvnQ3u60

######################   Reddit API    #########################


reddit = praw.Reddit(client_id='-edNsU3tljJDLg',
                     client_secret='jixbw6kbMbLZNlwFSvFkEjGU2JU', 
                     password='Rqwe123qwe!',
                     user_agent='PrawTut', 
                     username='jcflyingco')

subreddit = reddit.subreddit('Ebay')
hot_python = subreddit.hot(limit=10)
hot_python


# topic ID 
for submission in hot_python:
    print(submission)

# var 
for submission in hot_python:
    print(dir(submission))

# topic  title 
for submission in hot_python:
    print(submission.title)