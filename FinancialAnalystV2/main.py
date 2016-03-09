# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 2016
Author: Cedric Vallee
"""

import os
import re
import pandas as pd
import csv
import sklearn
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
from collections import defaultdict
import Matcher as matcher
import Validator as validator

# Function to create a list "dataset" with 3 columns: 'MD&A_Text','Filename','Sentiment'
def get_dataset(path):
    dataset=[]
    for filename in os.listdir(path):
        if filename.endswith("pos"):                             
            t = open(path + filename,"r").read() 
            dataset.append([re.sub('[^a-zA-Z]+', ' ', t), re.sub(r"(?:_pos)$",'', filename), "pos"])  
        elif filename.endswith("neg"):                          
            t = open(path + filename,"r").read()
            dataset.append([re.sub('[^a-zA-Z]+', ' ', t), re.sub(r"(?:_neg)$",'', filename), "neg"])                  
    return dataset

### Main function

# FEATURE 1 - Match with the McDonald Dictionary
dataset = get_dataset("../mdatest/")
dico = matcher.get_dico(dataset)        # dico is a column with the matching scores of the MDAs versus the Finance Dictionary 
df=pd.DataFrame(dataset)
df[3] = pd.Series(dico)
df.columns = ['MD&A_Text','Filename','Actual','MatchDico'] 

# FEATURE 2 and 3 - Match with the Compustat financial data to get the indices 'delta_sales' and 'delta_at'
compustat = pd.read_csv('compustat_filenames.csv', sep=',')
de = compustat['delta_sale']
dt = compustat['delta_at']
ds = pd.merge(df, compustat, left_on='Filename', right_on='Filename')


# We split the global matrix "result" into a training and a testing set
train, test = validator.split(ds,0.5)

# We fit a Random Forest model 	 (n_estimators default=10, min_samples_leaf default=1)
rf = RandomForestClassifier(n_estimators=100)
rf.fit(train[3].reshape(-1, 1), train[2].reshape(-1, 1))
predictions = rf.predict(test[3].reshape(-1, 1))
test[5] = pd.Series(predictions, index=test.index)

test.columns = ['MD&A_Text','Filename','Actual','MatchDico','WordCrisis','Predicted'] 
print(test)

tab = pd.crosstab(test['Actual'], test['Predicted'], rownames=['Actual'], colnames=['Predicted'], margins=True) # Print confusion matrix
print(tab)
print(classification_report(test['Actual'], test['Predicted'])) # Print accuracy, precision, recall, F measure