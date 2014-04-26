campaign_finance-state-OH
=========================

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
<li>delete the unzip option in the config file and create it as a subdirectory of download_dir.Change code accordingly.</li>
<li>add a test option as -t and move the json option to -j</li>
<li>find which tables are relevant - </li>
<li>for now - retrict tables to those with a year at the end of its name</li>
<li>change the file sructure if there are  multiple relevant table schemas so we can distribute json per table type.</li>
<li>Test a full download and address the inevitable errors.</li>
<li>Unit tests.</li>
<li>refactor</li>
</ul>



├── CAN  
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

