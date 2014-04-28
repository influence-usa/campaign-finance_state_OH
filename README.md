campaign_finance-state-OH
=========================
Issues
------
There are 3 types of files - CAN, PAR and PAC with to sub-types CON and EXP for each.
I am in the process of dividing these files associated json files into their  correct directory. The directory structure is
at the end of the README.
I'll try and have it all set to go in a few days.  
UPDATE:  
I've divided the filesystem to reflect the diffferent table types. Also there is a bad_date field provided in every
Year folder. The bad dates are mostly(if not all) empty date fields. note:the year is extracted from the file name.
Installation
------------
You must edit the config.py file and change the 3 paths:<br>
<b>download_dir</b> is the directory that the unzipped EXE files will be downloaded to.<br>
<b>unzipped_dir</b> is the directory that the downloaded EXE files will be extracted to. I make this directory a subdirectory of the <em>download_dir</em> - see above.<br>
<b>data_dir</b> is the directory that the final json files will be distributed to. 


To Use 
------
<blockquote>python run.py -p<print list>|-d<download>|-t<transform> & optional_Filter_String</blockquote>

Example print:
<blockquote><b>python run.py -p</b> <i> - prints all ftp files names and sizes.</i></blockquote>

<blockquote><b>python run.py -p 2009</b> 
<i>- prints all the names and sizes of all files with "2009" in the name.</i></blockquote>


Example download:
<blockquote><b>python run.py -d </b><i> - downloads all ftp files, unzips to csv and then distributes 1 json file per csv record. The json files are saved to Year and Quarter folders. The Year and Quarter folders are created during this process.</i></blockquote>   
<blockquote><b>python run.py -d 2009</b><i>
Downloads only files with "2009" in the name.</i></blockquote> 

Notes
-----
You should use the -p option first before downloading if this is your first time. If you use the -d option with no <em>Optional_filter_string</em> then all the ftp files wiill be downloaded and transformed. 
If you just want to do the csv to json tranformation then use the -t option. 

No file is overwritten in this process. If the file already exists then it is left alone. In order to do a fresh download and distribute of json files you must first delete all content from the 3 pathways found in your config.py.

TODO
----
<ul>
<li>delete the unzip path in the config file and create it as a subdirectory of download_dir.Change code accordingly.</li>
<li>add a test option as -t and move the json option to -j</li>
<li>find which tables are relevant - </li>
<li>for now - retrict tables to those with a year at the end of its name</li>
<li>change the file sructure if there are  multiple relevant table schemas so we can distribute json per table type.</li>
<li>Test a full download and address the inevitable errors.</li>
<li>Unit tests.</li>
<li>refactor</li>
</ul>


Example Directory structure created by Ohio download for 2009
--------------------------------------------------------------
├── CAN  
│   ├── CON  
│   │   └── 2009  
│   │       ├── PARTYEXPEND_DATE_NOT_FOUND  
│   │       ├── Q1  
│   │       ├── Q2  
│   │       ├── Q3  
│   │       └── Q4  
│   ├── EXP   
│   │   └── 2009  
│   │       ├── PARTYEXPEND_DATE_NOT_FOUND  
│   │       ├── Q1  
│   │       ├── Q2  
│   │       ├── Q3  
│   │       └── Q4  
├── PAC  
│   ├── CON  
│   │   └── 2009  
│   │       ├── PARTYEXPEND_DATE_NOT_FOUND  
│   │       ├── Q1  
│   │       ├── Q2  
│   │       ├── Q3  
│   │       └── Q4  
│   └── EXP  
│       └── 2009  
│           ├── PARTYEXPEND_DATE_NOT_FOUND  
│           ├── Q1  
│           ├── Q2  
│           ├── Q3  
│           └── Q4  
└── PAR  
    ├── CON  
    │   └── 2009  
    │       ├── PARTYEXPEND_DATE_NOT_FOUND  
    │       ├── Q1  
    │       ├── Q2  
    │       ├── Q3  
    │       └── Q4  
    └── EXP  
        └── 2009  
            ├── PARTYEXPEND_DATE_NOT_FOUND  
            ├── Q1  
            ├── Q2  
            ├── Q3  
            └── Q4  

