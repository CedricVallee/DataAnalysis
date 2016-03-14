# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 2016
Author: Cedric Vallee
"""

import os
import re
import pandas as pd
import csv
import Matcher as matcher

# Function to create a list of lists "dataset". Input: path. Output: pd.Dataframe.
def get_dataset(path):
    dataset=[]
    for filename in os.listdir(path):
        t = open(path + filename,"r").read() 
        dataset.append([filename, re.sub('[^a-zA-Z]+', ' ', t)])  
    dico = matcher.get_dico(dataset) # dico is a column with the matching scores of the MDAs versus the Finance Dictionary 
    df=pd.DataFrame(dataset)
    df[1] = pd.Series(dico)
    blob = matcher.get_blob(df)                   
    df[2] = pd.Series(blob)
    df.columns = ['Filename','MatchDico','TextBlob']
    return df

# Function to append the Compustat attributes to the dataframe. Input: pd.dataframe. Output: pd.dataframe.
def append_compustat(dataframe):
    compustat = pd.read_csv('compustat_40_days.csv', sep=',')
    df = pd.merge(dataframe, compustat, left_on='Filename', right_on='Filename')
    return df

# FEATURE 1 - Match with the McDonald Dictionary
# FEATURE 2 - TextBlob sentiment polarity score
df = get_dataset("../mda/")
# FEATURE 3 - Match with the Compustat financial data to get the indices 'delta_sales' and 'delta_at'
df = append_compustat(df)
# Save the dataframe as an MS Excel spreadsheet
df.to_csv('../matrix.csv', sep=',')
