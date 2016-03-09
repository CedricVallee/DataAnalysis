This folder contains code to run a financial analysis on 10-k reports. The workspace should be organized as follow:

data/    &emsp;              # Folder containing 10-k reports <br>
mda/     &emsp;              # Folder containing the MDA sections, scraped using extractMDA.py, Scraper.py and Helper.py <br>
v2.dictionary/ <br>
&emsp;  debug/               # Folder containing 10-k reports that extractMDA wasn't able to scrape <br>
&emsp;  LoughranMcDonald_MasterDictionary_2014.xlsx <br>
&emsp;  compustat_filenames  # csv file with Compustat financial data about companies in the 'Industrial Goods' sector <br>
&emsp;  extractMDA.py <br>
&emsp;  Scraper.py <br>
&emsp;  Helper.py <br>
&emsp;  Matcher.py <br>
&emsp;  Validator.py <br>
&emsp;  main.py <br>

<b>PRELIMINARY STEPS</b><br>
0A- MDA sections are extracted from the 10-k reports (folder 'data') and saved in the folder 'mda' using extractMDA.py
(which calls the classes Helper.py and Scraper.py).<br>
0B- The file compustat_filenames.csv is obtained by running SQL queries (see file 'queries.sql') on Compustat raw financial data. The columns 'delta_sales' and 'delta_at' are added using basic calculation on MS Excel (see slides).<br>
<br>
<b>RUNNING THE CODE</b><br>
1- Run main.py (which calls Matcher.py and Validator.py) to create a dataframe, add features such as matching with the Loughran and McDonald finance dictionary, and test the performance of a Random Forest Classifier. <br>
<br>
The folder 'mdatest' contains some examples of tagged mda sections which the reader can use as test files (to put in the folder "mda") for the functions in main.py
