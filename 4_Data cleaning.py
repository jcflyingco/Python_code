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



# Read the file into a DataFrame: df
df = pd.read_csv('C:/Users/tduan/Desktop/Mission/Python/data/DOB_Job_Application_Filings.csv')
# Print the head of df
print(df.head())
# Print the tail of df
print(df.tail())
# Print the shape of df
print(df.shape)
# Print the columns of df
print(df.columns)
# Print the info of df
print(df.info())
# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))
# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))
# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))


# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
plt.show()

# Create the boxplot
df.boxplot(column="Existing Zoning Sqft", by='Borough', rot=90)
plt.show()

# Create and display the first scatter plot
df.plot(kind='scatter', x="Existing Zoning Sqft", y="Proposed Zoning Sqft", rot=70)
plt.show()




















