# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 2016
Author: Cedric Vallee
"""

from sklearn.cross_validation import train_test_split

# Function to return a row from a list of lists
def split(df,test_ratio):
    return train_test_split(df, test_size = test_ratio)