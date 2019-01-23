# Import pandas 
# Keras Tutorial: Deep Learning in Python
# https://www.datacamp.com/community/tutorials/deep-learning-python#comments

# This tutorial is the one found on Datacamp (see link)
# I just added some comments and 2/3 compatibility modifications
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Seaborn is a Python visualization library based on matplotlib. 
# It provides a high- level interface for drawing attractive statistical graphics
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Dense


# Read in white wine data 
white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')

# Read in red wine data 
red = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

# Print info on white wine
# print(white.info())

# Print info on red wine
# print(red.info())

# First rows of `red` 
red.head()

# Last rows of `white`
# white.tail()

# Take a sample of 5 rows of `red`
# red.sample(5)

# Describe `white`
# white.describe()

# Double check for null values in `red`
# pd.isnull(red)