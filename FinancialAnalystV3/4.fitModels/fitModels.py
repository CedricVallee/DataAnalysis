# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 2016
Author: Cedric Vallee
"""

import pandas as pd
import csv
import Fitter as fitter
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

# Split the global matrix "result" into a training and a testing set
df = pd.read_csv('../matrix.csv', sep=',')
df = df.fillna(0)
train, test = fitter.split(df,0.5)
variables = ['MatchDico', 'TextBlob', 'delta_sale', 'delta_at']
target = ['Actual']

# MODEL 1 - Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100)
print('RANDOM FOREST CLASSIFIER')
fitter.fit_model(train, test, target, variables, rf)

# MODEL 2 - Gradient Boosting Classifier
gb = GradientBoostingClassifier(n_estimators=100)
print
print('GRADIENT BOOSTING CLASSIFIER')
fitter.fit_model(train, test, target, variables, gb)

# MODEL 3 - Logistic Regression
lr = LogisticRegression()
print
print('LOGISTIC REGRESSION')
fitter.fit_model(train, test, target, variables, lr)