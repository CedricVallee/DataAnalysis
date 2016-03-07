This folder contains code to run a financial analysis on 10-k reports. The workspace should be organized as follow:

data/    &emsp;              # Folder containing 10-k reports <br>
mda/     &emsp;              # Folder containing the MDA sections, scraped using extractMDA.py, Scraper.py and Helper.py <br>
v2.dictionary/ <br>
&emsp;  debug/ <br>
&emsp;  extractMDA.py <br>
&emsp;  Scraper.py <br>
&emsp;  Helper.py <br>
&emsp;  LoughranMcDonald_MasterDictionary_2014.xlsx <br>
&emsp;  Matcher.py <br>
&emsp;  Validator.py <br>
&emsp;  main.py <br>

The code should be run as follow:

1- Extract the MDA sections from the 10-k reports in the folder "data" using extractMDA.py 
(which calls the classes Helper.py and Scraper.py). The folder "mda" will fill up with the MDA sections. <br>
2- Run main.py (which calls Matcher.py and Validator.py) to create a dataframe, add features such as matching with the Loughran and McDonald finance dictionary, and test the performance of a Random Forest Classifier.
