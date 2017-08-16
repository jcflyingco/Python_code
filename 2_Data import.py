#   2 Data import

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
import json
import tweepy
import math

wd = os.getcwd()
wd
os.listdir(wd)

os.chdir('C:/Users/tduan/Desktop/Mission/Python/code')



##############   key in #######################
A=np.array([[1,23,344,1233],
           [2,33,441,1111],
           [9,10,222,6666]])

A

cal=A.sum(axis=0)
print(cal)
cal
cal.reshape(1,4)

percentage=100*A/cal.reshape(1,4)
percentage


################################################
###############      txt     ##################

filename="C:/Users/User/Desktop/Mission/Python/data/test001.txt"

txt001=np.loadtxt(filename,delimiter=',',skiprows=1)

################################################
###############    csv       ##################


file002='C:/Users/User/Desktop/Mission/Python/data/titanic_train.csv'

csv001=pd.read_csv(file002)
csv002 = pd.read_csv(file002, nrows=5, header=None)

#print(data)
print(csv001.head())
print(csv002.head())


# Plot 'Age' variable in a histogram
pd.DataFrame.hist(csv001[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()


###############################################
########################   excel ##############


# Assign spreadsheet filename: file
file="C:/Users/User/Desktop/Mission/Python/data/titanic_train_Part2.xlsx"


# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('tt001')
# Print the head of the DataFrame df1
print(df1.head())
# Load a sheet into a DataFrame by index: df2
df2 = xl.parse(0)
# Print the head of the DataFrame df2
print(df2.head())

# Parse the first sheet and rename the columns: df1
#df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])
# Print the head of the DataFrame df1
#print(df1.head())
# Parse the first column of the second sheet and rename the column: df2
df2 = xl.parse(0, parse_cols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())




#################################################
########################   SAS  #################

# Save file to a DataFrame: df_sas
with SAS7BDAT("C:/Users/User/Desktop/Mission/Python/data/airline.sas7bdat") as file:
    sas001 = file.to_data_frame()

# Print head of DataFrame
print(sas001.head())

# Plot histograms of a DataFrame feature (pandas and pyplot already imported)
pd.DataFrame.hist(sas001[['Y']])
plt.ylabel('count')
plt.show()


################################################
######################   HDF5   ###############


##################################################
#####################  matlab  ##################


# Load MATLAB file: mat
mat = scipy.io.loadmat('C:/Users/User/Desktop/Mission/Python/data/train_tt001.mat')
print(mat.keys())
# Print the datatype type of mat
print(type(mat))





np.log(3)
np.abs(-3)
np.maximum([1,2,3],2)


######################################################
#######################   Database ###################

####################### SQL Lite ####################

#Old 1
# Create engine: engine   
engine = create_engine('sqlite:///C:/Users/User/Desktop/Mission/Python/data/Chinook.sqlite')
# Save the table names to a list: table_names
table_names = engine.table_names()
# Print the table names to the shell
print(table_names)
# Open engine connection
con = engine.connect()
# Perform query: rs
rs = con.execute("SELECT * FROM Album")
# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.head()
con.close()

# Old 2
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()
# Print the length of the DataFrame df
print(len(df))
# Print the head of the DataFrame df
print(df.head())


#new 
##################  Pandas content 
engine = create_engine('sqlite:///Chinook.sqlite')
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)

# Print head of DataFrame
print(df.head())


# Execute query and store records in DataFrame: df
df = pd.read_sql_query(
    "SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000",
    engine
)
# Print head of DataFrame
print(df.head())


######################################################################
###########################     web         ########################



####################      web  csv  ################
# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Save file locally
urlretrieve(url, 'C:/Users/User/Desktop/Mission/Python/data/winequality-red.csv')
# Read file into a DataFrame and print its head
df = pd.read_csv('C:/Users/User/Desktop/Mission/Python/data/winequality-red.csv', sep=';')
print(df.head())
# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')
# Print the head of the DataFrame
print(df.head())

########################     web   excel ####################

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# Read in all sheets of Excel file: xl
xl = pd.read_excel(url, sheetname=None)
# Print the sheetnames to the shell
print(xl.keys())
# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())


#######################     web url  ######################

#old 
# Specify the url
url = "http://www.datacamp.com/teach/documentation"
# This packages the request: request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Print the datatype of response
print(type(response))
# Extract the response: html
html = response.read()
# Print the html
print(html)
# Be polite and close the response!
response.close()


#new 
# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"
# Packages the request, send the request and catch the response: r
r = requests.get(url)
# Extract the response: text
text = r.text
# Print the html
print(text)

######################    web Scrap    #########################
# Specify url: url
url = 'https://www.python.org/~guido/'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Get the title of Guido's webpage: guido_title
guido_title = soup.title
# Print the title of Guido's webpage to the shell
print(guido_title)
# Get Guido's text: guido_text
guido_text = soup.get_text()
# Print Guido's text to the shell
print(guido_text)
# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')
a_tags
# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))

########################    JSONs        #########################  

# Load JSON: json_data
with open('C:/Users/User/Desktop/Mission/Python/data/movie.json') as json_file:
    json_data = json.load(json_file)
    
type(json_data)
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


########################    API         #########################  

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])



# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Decode the JSON data into a dictionary: json_data
json_data = r.json()
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)




# Twitter API

# Store OAuth authentication credentials in relevant variables
access_token = "790128816647614464-Pu6fOFne0TbgEgxPpZdu7xXAW9tBhed"
access_token_secret = "6dJI4x5xUY47AmIj6ueMNd77Sew7fYYZBG9MnVxZ9eUkQ"
consumer_key = "EQr5kHd5JhQrsOvAk7x5Ak2LU"
consumer_secret = "LisjBswI88wuW0OV6LUkIJZkEOYKm7vSzqsJQWMQfXc3eKXwIy"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


#Here I define a Tweet listener that creates a file called 'tweets.txt', collects streaming tweets as .jsons and writes them to the file 'tweets.txt'; 
#once 100 tweets have been streamed, the listener closes the file and stops listening.
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")
    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()
    def on_error(self, status):
        print(status)


# Initialize Stream listener
l = MyStreamListener()
# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)
# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])
stream.filter(track=['ebay','eBay'])
# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'
# Initialize empty list to store tweets: tweets_data
tweets_data = []
# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())


# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])
df = pd.DataFrame(tweets_data)
# Print head of DataFrame
print(df.head())


