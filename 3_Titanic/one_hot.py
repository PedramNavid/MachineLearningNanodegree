# Testing one hot enconding

# In this exercise we'll load the titanic data (from Project 0)
# And then perform one-hot encoding on the feature names

import numpy as np
import pandas as pd

# Load the dataset
X = pd.read_csv('3_Titanic/titanic_data.csv')
# Limit to categorical data
X = X.select_dtypes(include=[object])

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# TODO: create a LabelEncoder

le = LabelEncoder()

# TODO: For each feature name in X, apply a label encoder using fit_transform
# Reassign this transformed data back into the feature for X!

X = X.apply(le.fit_transform)

# TODO: create a OneHotEncoder object, and fit it to all of X.
enc = OneHotEncoder()
enc.fit(X)

#TODO: transform the categorical titanic data, and store the transformed labels in the variable `onehotlabels`
onehotlabels = enc.transform(X).toarray()
