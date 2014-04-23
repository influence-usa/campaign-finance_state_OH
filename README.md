I NEED TO LEARN HOW TO EDIT an MD FILE.


campaign_finance-state-OH
=========================

To Use 

python run.py -p<print list>|-d<download>|-t<transform> & optional_Filter_String

example print:
---------------
python run.py -p "2009".

Will print all the names and sizes of all files with "2009" in the name.


example download:
----------------
python run.py -d  
What it does:downloads all files with an EXE extension from the OHIO site. Then those files are unzipped into csv files. Then the records from the csv files are distributed(json) into Year and Quarter folders that are created in your file system , if they don't currently exist.

>For testing you should use a Filter_string when downloading
>example: python run.py -d "2009"

Use the -p(print) flag first to scan the file names and sizes

If you just want to distribute the json files from the csv download, for instance , when testing then use
python run.py -t Filter_String 
.
1. First ordered list item
2. Another item
⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

reqiurements:
1.python 2.7*
2. NOT COMPLETED

Installation:
1. clone this repository.
2. check the config.py file.
3. create 3 directories.
..* one for EXE downloads.
..* one for uzipped EXE files in csv files (I make this a subdirectory of 1-above).
⋅⋅* one to house the json records that are broken out of the unzipped files(2 - above).
4. add directory paths to the config.py file.



The config.py file:
  A sample config.py file is cloned into your repository. 



Campaign finance in the Buckeye state

FOR NOW THIS IS A TODO FILE 
FIX README - I'll need help
unit_test
unzip process fails on at least one file. I will add an exception that will not kill the process of extracting.


MORE TO COME



