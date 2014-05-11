campaign_finance-state-OH
=========================
Installation
------------

<h4>Requirements</h4>
 unicodecsv is required to run this program.
<blockquote> pip install unicodecsv </blockquote>

<h4>Do Not Edit the config_File.py</h4>
You should  instead edit the config_local.py where you can overwrite(if nescessary) the following 3 variables:<br>
<b>DOWNLOAD_DIR</b> is the directory that the unzipped EXE files will be downloaded to.<br>
<b>UNZIPPED_DIR</b> is the directory that the downloaded EXE files will be extracted to. I make this directory a subdirectory of the <em>download_dir</em> - see above.<br>
<b>DATA_DIR</b> is the directory that the final json files will be distributed to.  




To Use 
------
<blockquote>python run.py -p<print>|-d<download>|-t<test>|-r<report> & optional_Filter_String</blockquote>

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
You should use the -p option first before downloading if this is your first time. If you use the -d option with no <em>Optional_filter_string</em> then all the ftp files will be downloaded and transformed.   
You can run future tests for this project with the <b>-t</b> flag (and no optional_filter_string) ex.  
<blockquote> python run.py -t </blockquote>  
You can run a report with the <b>-r</b> flag . The report breaks down the counts of files in each lowest level subdirectory.  Because this process takes
a while you should <b>USE THE </b> optional_Filter_string ex.  
<blockquote> python run.py -r 2009 </blockquote>  
No file is overwritten in this process. If the file already exists then it is left alone. In order to do a fresh download and distribute of json files you must first delete all content from the 3 pathways found in your config.py.

    Directory Structure 
    -------------------
    If you do not override the config.py default directories the the directory structure(shown at the end of the README) will be created within the campaign-finance_state_OH directory
    If you do override the config.py variables then remember to change the USE_ALTERNATE variable to True.

    Bad Dates
    ------
    there is a bad_date field provided in every
    Year folder. The bad dates are mostly(if not all) empty date fields. note:the year is extracted from the file name.

    Files That Are Used
    -------------------
    Currently there are files excluded from this process. Specifically files with 'MSTRKEY' in their name.
    This is the regex string used to filet the ftp files:('(?=ALL.*(19|20)\d{2})(?=.*(^(?!.*?MSTRKEY)))')

TODO
----
<ul>
<li>
The name campaign-finance_state_OH should be changed because python can't handle dashes in namespaces(I think?)
</li>
<li>Add an option to see all files on the FTP site</li>
<li>Figure out how to do file system graphs in MD(for this readme)</li>
<li>Find out if some files I am excluding are in fact relevant</li>
<li>Test a full download and address the inevitable errors.</li>
<li>Unit tests.</li>
<li>refactor</li>
</ul>


Example Directory structure created by Ohio download for 2009
--------------------------------------------------------------
.
Data
├── CAN
│   ├── CON
│   │   └── 2009
│   │       ├── BAD_DATE
│   │       ├── Q1
│   │       ├── Q2
│   │       ├── Q3
│   │       └── Q4
│   └── EXP
│       └── 2009
│           ├── BAD_DATE
│           ├── Q1
│           ├── Q2
│           ├── Q3
│           └── Q4
├── PAC
│   ├── CON
│   │   └── 2009
│   │       ├── BAD_DATE
│   │       ├── Q1
│   │       ├── Q2
│   │       ├── Q3
│   │       └── Q4
│   └── EXP
│       └── 2009
│           ├── BAD_DATE
│           ├── Q1
│           ├── Q2
│           ├── Q3
│           └── Q4
└── PAR
    ├── CON
    │   └── 2009
    │       ├── BAD_DATE
    │       ├── Q1
    │       ├── Q2
    │       ├── Q3
    │       └── Q4
    └── EXP
        └── 2009
            ├── BAD_DATE
            ├── Q1
            ├── Q2
            ├── Q3
            └── Q4

