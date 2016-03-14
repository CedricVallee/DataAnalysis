<p><b>Instructions</b></p>

This folder contains code to run a financial analysis on 10-k reports. The workspace should be organized as follow:

data/    &emsp;              # Folder containing 10-k reports <br>
mda/     &emsp;              # Folder containing the MDA sections, scraped using extractMDA.py, Scraper.py and Helper.py <br>
matrix.csv  &emsp;           # Global matrix containing all our features<br>
2.scrapeMDA/<br>
&emsp;  debug/               # Folder containing 10-k reports that extractMDA wasn't able to scrape <br>
&emsp;  extractMDA.py <br>
&emsp;  Helper.py <br>
&emsp;  Scraper.py <br>
3.createMatrix/<br>
&emsp;  compustat_40_days.csv <br>
&emsp;  LoughranMcDonald_MasterDictionary_2014.csv <br>
&emsp;  createMatrix.py <br>
&emsp;  Matcher.py <br>
4.fitModels/<br>
&emsp;  fitModels.py <br>
&emsp;  Fitter.py <br>

<p><b>0.extractZIP</b><br>
Download all relevant 10-k reports from ftp://ftp.sec.gov/edgar/full-index/ and save them in the 'data' folder.<br>
11 152 / 11 172 => 0.0017% error in our matching (Sector: Industrials. Code: 20).</p>

<p><b>1.labelReports</b><br>
We defined three tags: 'sell', 'hold' and 'buy'. Each 10-k report is allocated a tag by financial analysts and these decisions are available on Compustat. The .csv file containing Compustat data is named 'compustat_40_days.csv' and placed in the folder '3.createMatrix'.</p>

<p><b>2.scrapeMDA</b><br>
Most files are scraped by extractMDA.py, which calls Helper.py and Scraper.py <br>
The rest of the files (633 out of 11,152) raised exceptions and are placed in the 'debug' folder, to be analyzed manually.<br>
10 520/ 11 152
</p>

<p><b>3.createMatrix</b><br>
The Loughran and McDonald's dictionary was saved as 'LoughranMcDonald_MasterDictionary_2014.csv'.<br>
extractMatrix.py calls Matcher.py and merges all our data (Compustat data from step 1., matching score with the dictionary thanks to MDA sections scraped in step 2.) to create a global matrix, saved as "matrix.csv".<br></p>

<p><b>4.fitModels</b><br>
fitModels.py calls Fitter.py and tests different classifying models: sklearn.ensemble Random Forest Classifier, sklearn.ensemble Boosting Gradient Classifier, sklear.linear_model Logistic Regression.</p>

<p>
Notes: <br>
In the code, we use the following denomination: "dataset" refers to a list of lists, "dataframe" to a pandas dataframe.</p>
