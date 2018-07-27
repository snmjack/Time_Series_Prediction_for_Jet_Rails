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
