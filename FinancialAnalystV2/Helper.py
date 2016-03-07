# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 2016
Author: chongwee
Modified by Cedric Vallee Feb 29 2016
"""

import csv
import os

def writeDictOfListsToCSV(filename,dictionary):
    headers = sorted(dictionary.keys())
    with open(filename, 'w', newline="\n") as csvfile: 
        writer = csv.writer(csvfile.encode('UTF-8'))        
        for header in headers:
            cells = [header]
            cells.extend(dictionary[header])
            writer.writerow(cells)
    
def writeToFile(filename, text):    
    outputFile = open(filename, "w")
    outputFile.write(text.encode('UTF-8'))
    outputFile.close()

def writeToDirectoryFile(directory, filename, text):    
    if not os.path.exists(directory):
        os.makedirs(directory)
    outputFile = open(os.path.join(directory,filename), "w")
    outputFile.write(text.encode('UTF-8'))
    outputFile.close()

def readFromFile(directory,filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    inputFile = open(os.path.join(directory,filename), "r")
    fullText = inputFile.read()
    inputFile.close()    
    return fullText

#function to read the text file containing the Computstat company names and GICS code
def readInputsTXT(filepath,gics):
    gicsInputs = {}    
    with io.open(filepath, 'r', newline='\n') as f:
        reader = csv.reader(f.encode('UTF-8'),delimiter='\t')
        for row in reader:
            if row[2] is not None and row[2] == gics and row[0] not in gicsInputs.keys():
                gicsInputs[row[0]] = row[1]
    return gicsInputs

#function to read the list of filenames contained in the 10-K zip file
def readSECCSV(filepath):
    secInputs = []    
    with open(filepath, 'r', newline='\n', encoding="utf-8") as f:
        reader = csv.reader(f.encode('UTF-8'),delimiter='\t')
        for row in reader:            
            secInputs.append(row[0])
    f.close()
    return secInputs

def checkFileExists(directory,filename):
    if not os.path.exists(os.path.join(directory,filename)):
        return False
    else:
        return True

#function to tokenize the filenames of the 10-K documents, 
#extracts key information such as the company names used by SEC
def tokenizeFilenames(filename):
    attributes = {}    
    filename = filename.replace('sec-10-k/','')
    tokens = filename.split('_')
    if len(tokens) > 1:
        attributes['year'] = tokens[0]    
        attributes['qtr'] = tokens[1]    
        attributes['code'] = tokens[2]    
        attributes['name'] = tokens[3]    
        attributes['form'] = tokens[4]    
        attributes['date'] = tokens[5]    
        return attributes
    else:
        return None