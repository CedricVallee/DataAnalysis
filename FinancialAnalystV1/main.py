# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 2016
Author: Cedric Vallee
"""

import os
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import Scraper as scraper
import Helper as helper

# The naive Bayes classifier from last week was just checking if a word was present or not in the text.
# MultinomialNB will help us create a naive Bayes classifier evaluating a text according to the number of times a word appears.

# The folder Data contains all the financial reports we downloaded during the previous week (sector: Industrial Gooods; code:20)
# We manually added a suffix '_neg' or '_pos' to the name of a report according to its sentiment polarity.

# Function to scrape the MDAs from the reports (inspired by Chong Wee Tan Group 7)
def getMDAfromText(filename,text):
    try:
        soup = BeautifulSoup(text, "lxml")    
        fullText = scraper.scrapeByAnchorTag(soup)
        if fullText is not None:
            print("{0}\tScraped By Anchor".format(filename))
            return fullText
        fullText = scraper.scrapeByRegex(soup)
        if fullText is not None:
            print("{0}\tScraped By Regex".format(filename))
            return fullText
        if fullText is None:    
            print("{0}\tUnable to scrape".format(filename))
            text = ''.join(soup.findAll(text=True))
            text.replace("&#146;","'")
            helper.writeToDirectoryFile("debug",filename.replace("sec-10-k/",""),text)
        return None
    except UnicodeEncodeError:
        print("{0}\tUnicodeEncodeError".format(filename))
        return None

# Function to put the MDAs in a panda frame
def get_dataset(path):
    dataset=[]
    for filename in os.listdir(path):
        if filename.endswith("pos"):                                    # If report is tagged as positive
            doc = open(path + filename,"r")
            mda = getMDAfromText(filename,doc)
            if mda is not None:     
                soup = BeautifulSoup(mda, "html.parser")
                t=soup.get_text()
                dataset.append([re.sub('[^0-9a-zA-Z]+', '', t),filename,"pos"])  
        elif filename.endswith("neg"):                                  # If report is tagged as negative
            doc = open(path + filename,"r")
            mda = getMDAfromText(filename,doc)
            if mda is not None: 
                soup = BeautifulSoup(mda, "html.parser")
                t=soup.get_text()
                dataset.append([re.sub('[^0-9a-zA-Z]+', '', t),filename,"neg"])                  
    dataset.append(['The crisis lack deceiving unpredictable bad bad bad','test1','neg'])
    dataset.append(['the crisis non compliance losses','test2','neg'])
    dataset.append(['We lost thousands of dollars and exited exit','test3','neg'])                  
    dataset.append(['The company is ruined and we filed bankruptcy','test4','neg'])
    dataset.append(['We modified our plans since results from last year were bad','test5','neg'])
    dataset.append(['niche and unique opportunity to grow and grow develop acquisition acquisitions and contracts good prospects','test6','pos'])
    dataset.append(['encouraging results and better outlook promising sales and new market main actor first','test7','pos'])
    dataset = pd.DataFrame(dataset)
    dataset.columns = ['MD&A_Text','Filename','Sentiment']                     # Return the pd.DataFrame obtained from the list
    return dataset

# Function to split the dataset into training and testing set
def split(df,test_ratio):
    return train_test_split(df, test_size = test_ratio)

    
### Main function
dataset = get_dataset("../data/")
train, test = split(dataset,0.5)

vectorizer = CountVectorizer(stop_words="english",max_features = 50) # Build a vocabulary that only consider the top max_features ordered by term frequency across the corpus
counts = vectorizer.fit_transform(train['MD&A_Text'].values)
classifier = MultinomialNB(fit_prior="False")                   # Should we put fit_prior True or False? If False, a uniform prior will be used.
targets = train['Sentiment'].values
classifier.fit(counts, targets)

counts_test = vectorizer.transform(test['MD&A_Text'].values)
predictions = classifier.predict(counts_test) 

test['Prediction'] = pd.Series(predictions, index=test.index)

print(test)                                                         # Print result dataframe (filenames, actual and predicted sentiments)
tab = pd.crosstab(test['Sentiment'], test['Prediction'], rownames=['Actual'], colnames=['Predicted'], margins=True) # Print confusion matrix
print(tab)
print(classification_report(test['Sentiment'], test['Prediction'])) # Print accuracy, precision, recall, F measure
