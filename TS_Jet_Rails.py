# ---------------------------  IMPORTS  -------------------------------------- #
# Import Mathematical Libraries
import pandas as pd         # For DataFrames          
import numpy as np          # For mathematical calculations
from pandas import Series        # To work on series

# Import Plotting Libraries
import matplotlib.pyplot as plt  # For plotting graphs
%matplotlib inline

# Import Warning Filter Libraries
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")

# Import DateTime Libraries
from datetime import datetime    # To access datetime


# ---------------------------  LOAD DATA  -------------------------------------- #
''' After Downloading the data from
https://datahack.analyticsvidhya.com/contest/practice-problem-time-series-2/
We have two - Train_SU63ISt and Test_0qrQsBZ CSV files
'''

# Read CSV file to Pandas Dataframe
train=pd.read_csv("Train_SU63ISt.csv")
test=pd.read_csv("Test_0qrQsBZ.csv")

# Make Copy of the original Dataframe to process on it furthur
train_original=train.copy()
test_original=test.copy()

# ---------------------------  CHECK DATA for TYPE, SHAPE  -------------------------------------- #
train.columns, test.columns

train.dtypes, test.dtypes

train.shape, test.shape

# ---------------------------  FEATURE EXTRACTION  -------------------------------------- #

# Convert the Datetime Object in DataFrame to Date and Time format for Time Series Analysis
train['Datetime'] = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
test['Datetime'] = pd.to_datetime(test.Datetime,format='%d-%m-%Y %H:%M') 
test_original['Datetime'] = pd.to_datetime(test_original.Datetime,format='%d-%m-%Y %H:%M')
train_original['Datetime'] = pd.to_datetime(train_original.Datetime,format='%d-%m-%Y %H:%M')

# Furthur breakdown Date and Time in Year, Month, Day , Hours
for i in (train, test, test_original, train_original):
    i['year']=i.Datetime.dt.year 
    i['month']=i.Datetime.dt.month 
    i['day']=i.Datetime.dt.day
    
    
    i['Hour']=i.Datetime.dt.hour 
