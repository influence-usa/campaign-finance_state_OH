campaign_finance-state-OH
=========================

To Use 

python run.py -p<print list>|-d<download> & optional_Filter_String

example print:<br>

python run.py -p "2009" <br>

Will print all the names and sizes of all files with "2009" in the name.<br>


example download:<br>
python run.py -d "2009" <br>

Will download all files with "2009" in the name.<br>


I suggest using the -p(print) flag first to see what is available.<br>


Campaign finance in the Buckeye state

FOR NOW THIS IS A TODO FILE 
describe the config file in this readme
only download files not already existing
create year and quarters directories and distribute json files acordingly.
unit_test
unzip process fails on at least one file. I will add an exception that will not kill the process of extracting.

Right now the json transformation only works for one sample file. I'll change  this to loop over all the files and use
the Year/Quarter protocol.

MORE TO COME



