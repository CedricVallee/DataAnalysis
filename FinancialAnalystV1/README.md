This folder contains a first basic version of a program which analyzes 10-k financial reports of companies. 
The aim of the program is to determine if companies do well (pos) or bad (neg) by running a text analysis of the "Management's Discussion and Analysis" section of the reports.

The Helper and Scraper classes were written by chongwee83, to scrape the HTML MDA sections from reports.
The main function runs a Multinomial naive Bayes classifier on words, and tests the accuracy, precision, recall and F measure of the model.
(names of the financial reports should end with "_pos" or "_neg" to show their actual polarity)
