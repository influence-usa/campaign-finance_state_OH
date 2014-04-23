

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

example print:
<blockquote><b>python run.py -p</b> <i> - prints all ftp files names and sizes.</i></blockquote>

<blockquote><b>python run.py -p 2009</b> 
<i>- prints all the names and sizes of all files with "2009" in the name.</i></blockquote>


example download:
<blockquote><b>python run.py -d </b><i> - downloads all ftp files, unzips to csv and then distributes 1 json file per csv record. The json files are saved to Year and Quarter folders. The Year and Quarter folders are created during this process.</i></blockquote>   
<blockquote><b>python run.py -d 2009</b><i>
Downloads only files with "2009" in the name.</i></blockquote> 





