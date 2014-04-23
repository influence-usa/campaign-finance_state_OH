


campaign_finance-state-OH
=========================

Installation
------------
You must edit the config.py file and change the 3 paths:<br>



To Use 
------
python run.py -p<print list>|-d<download>|-t<transform> & optional_Filter_String

example print:
---------------
>python run.py -p
prints all ftp files names and sizes.

>python run.py -p 2009
Will print all the names and sizes of all files with "2009" in the name.


example download:
----------------
>python run.py -d  
Downloads all ftp files, unzips to csv and then distributes 1 json file per csv record. The json files are saved to Year and Quarter folders. The Year and Quarter folders are created during this process.   
>python run.py -d 2009
Downloads only files with "2009" in the name. 





