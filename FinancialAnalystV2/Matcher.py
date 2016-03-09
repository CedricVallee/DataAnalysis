# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 2016
Author: Cedric Vallee
"""

import re
import pandas as pd
import csv
import sklearn
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from collections import defaultdict

# Function to return a row from a list of lists
def get_column(listOfLists, i):
    return [row[i] for row in listOfLists]
  
# FEATURE 1 - Match with the McDonald Dictionary

def matchDictionary(tfidf_df):
    # Reading the Loughran-McDonalds dictionary of finance-specific words
    dict = pd.read_excel("LoughranMcDonald_MasterDictionary_2014.xlsx")
    minidict = dict[dict['Word'].isin(tfidf_df.columns)] 
    minidict = minidict.set_index('Word')
    # We don't care for the years
    minidict.loc[minidict['Positive']>0, 'Positive'] = 1
    minidict.loc[minidict['Negative']>0, 'Negative'] = -1
    # Just some transformations to facilitate merging
    tfidf_df = tfidf_df.T 
    tfidf_df.index.name='Word'
    # Match the tf.idf matrix with finance-specific dictionary and score the sentences
    result_df = pd.merge(tfidf_df, minidict, how='left', left_index=True, right_index=True)
    return result_df
    
def get_dico(dataset):
    corpus = get_column(dataset,0)
    # Calculate raw word counts, remove stop words
    tf = TfidfVectorizer(analyzer='word', min_df = 0, stop_words = 'english')
    # Create a sparse matrix with (nrows = nb of documents, ncol = nb of disctinct words no stop-words)
    tfidf_matrix =  tf.fit_transform(corpus)
    feature_names = tf.get_feature_names() 
    tfidf_array = tfidf_matrix.toarray()
    tfidf_df = pd.DataFrame(tfidf_array)
    # Store all the words in uppercase
    tfidf_df.columns = [i.upper() for i in feature_names]
    result_df = matchDictionary(tfidf_df)
    dico=[]
    for i in range(0, len(corpus)):
        dico.append(np.nansum(result_df[i]*(result_df['Positive']-result_df['Negative'])))
    return dico
 