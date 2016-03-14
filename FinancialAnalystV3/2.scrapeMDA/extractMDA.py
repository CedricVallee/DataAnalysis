# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 2016
@author: Cedric Vallee
Inspired by Chong Wee Tan
"""

import os
import Helper as helper
import Scraper as scraper
from textblob import TextBlob
from bs4 import BeautifulSoup

def getMDAfromText(filename,text):
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
            helper.writeToDirectoryFile("debug",filename,text)   
        return None

# Function to create a folder named 'mda' with all the MDAs extracted from reports in the 'data' folder, using the previous function [path = "../data/"]
def createMDAfiles(path):
    for filename in os.listdir(path):      
        text = open(path + filename).read()
        mdaText = getMDAfromText(filename,text)
        if mdaText is not None:
            helper.writeToDirectoryFile("../mda/",filename,mdaText)

# Main function
createMDAfiles("../data/")