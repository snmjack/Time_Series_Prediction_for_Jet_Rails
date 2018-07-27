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
    
# Adding additional feature of Weekdaya and Weekend. 
train['day of week']=train['Datetime'].dt.dayofweek
temp = train['Datetime']

# No. 5 & 6 will be weekend, so replace it with 1 
def applyer(row):
    if row.dayofweek == 5 or row.dayofweek == 6:
        return 1
    else:
        return 0

# Apply the values of Weekdays as 0 and Weekend as 1 
temp2 = train['Datetime'].apply(applyer)
train['weekend']=temp2


# ---------------------------  EXPLORATOORY DATA ANALYSIS (EDA)  -------------------------------------- #

# Plotting of Count of passenger on time axis
train.index = train['Datetime'] # indexing the Datetime to get the time period on the x-axis.
df=train.drop('ID',1)           # drop ID variable to get only the Datetime on x-axis.
ts = df['Count']
plt.figure(figsize=(16,8))
plt.plot(ts, label='Passenger Count')
plt.title('Time Series')
plt.xlabel("Time(year-month)")
plt.ylabel("Passenger count")
plt.legend(loc='best')

# Year wise customer count plot
train.groupby('year')['Count'].mean().plot.bar()

# Month wise customer count plot
train.groupby('month')['Count'].mean().plot.bar()

# Monthly mean of each year seperately
temp=train.groupby(['year', 'month'])['Count'].mean()
temp.plot(figsize=(15,5), title= 'Passenger Count(Monthwise)', fontsize=14)

# Day Wise customer count plot
train.groupby('day')['Count'].mean().plot.bar()

# Hour wise customer count plot
train.groupby('Hour')['Count'].mean().plot.bar()

# Weekend and Weekday Plot
train.groupby('weekend')['Count'].mean().plot.bar()

# Every day of the week customer count plot
train.groupby('day of week')['Count'].mean().plot.bar()

# ---------------------------  AGGREGATE HOURLY DATA TO DAILY, WEEKLY AND MONTHLY  -------------------------------------- #
train=train.drop('ID',1)
train.Timestamp = pd.to_datetime(train.Datetime,format='%d-%m-%Y %H:%M') 
train.index = train.Timestamp

hourly = train.resample('H').mean()  # Hourly time series
daily = train.resample('D').mean()   # Converting to daily mean
weekly = train.resample('W').mean()  # Converting to weekly mean
monthly = train.resample('M').mean() # Converting to monthly mean


# Plot Hourly, Daily, Weekly and Monthly data
fig, axs = plt.subplots(4,1)
hourly.Count.plot(figsize=(15,8), title= 'Hourly', fontsize=14, ax=axs[0])
daily.Count.plot(figsize=(15,8), title= 'Daily', fontsize=14, ax=axs[1])
weekly.Count.plot(figsize=(15,8), title= 'Weekly', fontsize=14, ax=axs[2])
monthly.Count.plot(figsize=(15,8), title= 'Monthly', fontsize=14, ax=axs[3])
plt.show()


