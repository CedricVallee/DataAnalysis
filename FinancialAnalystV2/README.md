This folder contains code to run a financial analysis on 10-k reports. The workspace should be organized as follow:

data/                     # Folder containing 10-k reports
mda/                      # Folder containing the MDA sections, scraped using extractMDA.py, Scraper.py and Helper.py
v2.dictionary/
  debug/
  extractMDA.py
  Scraper.py
  Helper.py
  LoughranMcDonald_MasterDictionary_2014.xlsx
  Matcher.py
  main.py

The code should be run as follow:

1- Extract the MDA sections from the 10-k reports in the folder "data" using extractMDA.py 
(which calls the classes Helper.py and Scraper.py). The folder "mda" will fill up with the MDA sections.
2- 
