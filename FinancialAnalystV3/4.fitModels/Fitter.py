# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 2016
Author: Cedric Vallee
"""

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Function to split data between a training and a testing set
def split(df,test_ratio):
    return train_test_split(df, test_size = test_ratio)
    
# Function to create Classification Report (Group 7)
def fit_model(train, test, target, variables, classifier):
    tarTrain = train.as_matrix(target)
    varTrain = train.as_matrix(variables)
    classifier.fit(varTrain,tarTrain)
    varTest = test.as_matrix(variables)
    predictions = classifier.predict(varTest)
    # Print confusion matrix
    tab = pd.crosstab(test['Actual'], predictions, rownames=['Actual'], colnames=['Predicted'], margins=True)
    print(tab)
    # Print accuracy, precision, recall, F measure
    print(classification_report(test['Actual'], predictions))
    a=accuracy_score(test['Actual'],predictions)
    p=precision_score(test['Actual'],predictions, pos_label = "pos")
    r=recall_score(test['Actual'].values,predictions, pos_label = "pos")
    f=f1_score(test['Actual'].values,predictions, pos_label = "pos")
    print "Accuracy = ",a,"\nPrecision =",p,"\nRecall = ",r,"\nF-Score = ",f 
   
