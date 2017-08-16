##########   Data Pipeline ########################


#   1 Package    
#   2 Data import
#   3 Data EDA & visualization
#   4 Data Cleaning
#   5 Data Modeling
#   6 Model Vaildation
#   7 Model scoring
#   8 Data output &presentation

###########################################################

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




###########  3 Data EDA & visualization   ####################


from bokeh.plotting import figure
from bokeh.io import output_file, show




file="C:/Users/tduan/Desktop/Mission/Python/data/fertility.xlsx"

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

fertility = xl.parse('Sheet1')

fertility.head()

print(fertility.columns)

# Create the figure: p
p = figure(x_axis_label='fertility (children per woman)', y_axis_label='female_literacy (% population)')

# Add a circle glyph to the figure p
p.circle('fertility', 'female literacy')

# Call the output_file() function and specify the name of the file
output_file('fert_lit.html')

# Display the plot
show(p)




