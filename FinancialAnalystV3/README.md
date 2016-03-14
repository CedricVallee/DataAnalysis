<p><b>Instructions</b></p>

<p><b>0.extractZIP</b><br>
Download all relevant 10-k reports from ftp://ftp.sec.gov/edgar/full-index/ and save them in the 'data' folder.</p>

<p><b>1.labelReports</b><br>
We defined three tags: 'sell', 'hold' and 'buy'. Each 10-k report is allocated a tag by financial analysts and these decisions are available on Compustat. The .csv file containing Compustat data is named 'compustat_40_days.csv' and placed in the folder '3.createMatrix'.</p>

<p><b>2.scrapeMDA</b><br>
Files are scraped by extractMDA.py, which calls Helper.py and Scraper.py <br>
The rest of the files (5 out of 11,000) raised exceptions and are placed in the 'debug' folder, to be analyzed manually.</p>

<p><b>3.createMatrix</b><br>
The Loughran and McDonald's dictionary was saved as 'LoughranMcDonald_MasterDictionary_2014.csv'.<br>
extractMatrix.py calls Matcher.py and merges all our data (Compustat data from step 1., matching score with the dictionary thanks to MDA sections scraped in step 2.) to create a global matrix, saved as "matrix.csv".<br></p>

<p><b>4.fitModels</b><br>
fitModels.py calls Fitter.py and tests different classifying models: sklearn.ensemble Random Forest Classifier, sklearn.ensemble Boosting Gradient Classifier, sklear.linear_model Logistic Regression.</p>

<p>
Notes: <br>
In the code, we use the following denomination: "dataset" refers to a list of lists, "dataframe" to a pandas dataframe.</p>
