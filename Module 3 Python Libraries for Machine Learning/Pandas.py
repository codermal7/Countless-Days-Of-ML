# -*- coding: utf-8 -*-
"""Complete Pandas Tutorial in Python

Pandas Library:

Useful for Data Processing & Analysis

Pandas Data Frame:

Pandas DataFrame is two-dimensional tabular data structure with labeled axes (rows and columns).
"""

# importing the pandas library
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np

"""Creaating a Pandas DataFrame"""

# importing the boston house price data

boston_dataset = load_boston()

type(boston_dataset)

print(boston_dataset)

# pandas DataFrame
boston_df = pd.DataFrame(
    boston_dataset.data, columns=boston_dataset.feature_names)

boston_df.head()

boston_df.shape

type(boston_df)

"""Importing the data from a CSV file to a pandas DataFrame"""

# csv file to pandas df
diabetes_df = pd.read_csv('/content/diabetes.csv')

type(diabetes_df)

diabetes_df.head()

diabetes_df.shape

"""Loading the data from a excel file to a Pandas DataFrame:

pd.read_excel('file path')

Exporting a DataFrame to a csv file
"""

boston_df.to_csv('boston.csv')

"""Exporting the Pandas DataFrame to an excel File:

df.to_excel('filename')
"""

# creating a DatFrame with random values
random_df = pd.DataFrame(np.random.rand(20, 10))

random_df.head()

random_df.shape

"""Inspecting a DataFrame"""

# finding the number of rows & columns
boston_df.shape

# first 5 rows in a DataFrame
boston_df.head()

# last 5 rows of the DataFrame
boston_df.tail()

# informations about the DataFrame
boston_df.info()

# finding the number of missing values
boston_df.isnull().sum()

# diabetes dataframe
diabetes_df.head()

# counting the values based on the labels
diabetes_df.value_counts('Outcome')

# group the values based on the mean
diabetes_df.groupby('Outcome').mean()

"""Statistical Measures"""

# count or number of values
boston_df.count()

# mean value - column wise
boston_df.mean()

# standard deviation - column wise
boston_df.std()

# minimum value
boston_df.min()

# maximum value
boston_df.max()

# all the statistical measures about the dataframe
boston_df.describe()

"""Manipulating a DataFrame"""

# adding a column to a dataframe
boston_df['Price'] = boston_dataset.target

boston_df.head()

# removing a row
boston_df.drop(index=0, axis=0)

# drop a column
boston_df.drop(columns='ZN', axis=1)

# locating a row using the index value
boston_df.iloc[2]

# locating a particular column
print(boston_df.iloc[:, 0])  # first column
print(boston_df.iloc[:, 1])  # second column
print(boston_df.iloc[:, 2])  # third column
print(boston_df.iloc[:, -1])  # last column

"""Correlation:

1. Positive Correlation
2. Negative Correlation
"""

boston_df.corr()
