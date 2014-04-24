import glob
import zipfile
import config
from ftplib import FTP
import os, sys, os.path
import re
import json
import unicodecsv
from datetime import datetime
#WARNING THIS WILL TAKE A WHILE TO RUN
class Ohio(object):
    def __init__(self,filter=''): 
        self.filter =  filter
        self.ftp = FTP("serproxy.sos.state.oh.us") # no pass
        self.ftp.login()
        self.ftp.cwd("/free")
        self.filenames = []
        self.ftp.retrlines('NLST', self.filenames.append)
        self.unzipped_dir = config.unzipped_dir
        self.data_dir = config.data_dir
        self.download_dir = config.download_dir

    def __del__(self):
        self.ftp.close()
        print "OHIO ftp closed"
    def print_ftp(self):
        for files in self.list_ftp():
            print files[0] + " - FileSize:" + str(files[1])

    def download_ftp(self):
        for filename in self.list_ftp():
            local_filename = os.path.join( self.download_dir, filename[0])
            if os.path.isfile(local_filename) is True:
                print filename[0] + " already exists."
            else:
                print 'opening ' +  filename[0]
                file = open(local_filename, 'wb')
                print 'creating ' +   filename[0]
                print "....................."
                self.ftp.retrbinary('RETR '+ filename[0], file.write)
   
    def list_ftp(self):
        str = '.*' + self.filter  + '.*\\.EXE'
        regex = re.compile(str)
        for filename in self.filenames:
            if re.match(regex, filename.upper()):
                yield filename,self.ftp.size(filename)

    def unzip_files(self):
        for zip_filename in self.list_ftp():
            print 'unzipping ' + zip_filename[0]
            zip_handler = zipfile.ZipFile(self.download_dir + "/" + zip_filename[0], "r")
            zip_handler.extractall(config.unzipped_dir)

    def get_ftp(self):
        self.download_ftp()
        self.unzip_files()
        self.extract_json_files()

    def get_quarter(self,date_str):
        dt = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
      #  gen = ((i+1,[j, j+1,j+2]) for i,j in enumerate([1, 4, 7,10]))
      #  print list(gen)
        q_gen = [ [i+1,x] for i,j in enumerate([1, 4, 7,10] )for x in range(j,j+3)] 
        for x in q_gen:
            if dt.date().month == x[1]:
                return x[0]
        return False           

    def extract_json_files(self):
         #SEE LATIN1 BELOW! Change this depending on the data
        failures = 0    
        print  "extracting " + str(sum(1 for x in self.list_ftp())) +  " csv files to json"
        for filename in self.list_ftp():
            filename = filename[0].replace(".EXE",".CSV")
            print  "extracting " +  filename + " to json"
            try:
                input_file = unicodecsv.DictReader(open(config.unzipped_dir + "/" + filename), encoding='latin1')
            except:
                print  filename  + " from the ftp site does not exist in your local directories so json extraction is skipped for " + filename + "."
                input_file = ""
                failures += 1

            for (x, d) in enumerate(input_file):
                d['id']=x
                if  'PARTYEXPEND_DATE' in d:
                    Q = "Q" + str(self.get_quarter(d['PARTYEXPEND_DATE']))
                else:
                    Q = 'PARTYEXPEND_DATE_NOT_FOUND' 

                if not os.path.exists(self.data_dir + "/" + d['RPT_YEAR']):
                    os.makedirs(self.data_dir + "/" + d['RPT_YEAR'])
                    for i in range(1, 5):
                        if not os.path.exists(self.data_dir + "/" + d['RPT_YEAR'] + "/Q" + str(i)):
                            os.makedirs(self.data_dir + "/" + d['RPT_YEAR'] + "/Q" + str(i))

                if not os.path.exists(self.data_dir + "/" + d['RPT_YEAR'] + "/PARTYEXPEND_DATE_NOT_FOUND" ):
                    os.makedirs(self.data_dir + "/" + d['RPT_YEAR'] + "/PARTYEXPEND_DATE_NOT_FOUND" )

                with open( self.data_dir + "/" + d['RPT_YEAR'] + "/" + Q + "/" +  str(d['id']) + '.json', 'w') as outfile:
                    json.dump(d, outfile)

        print str(sum(1 for x in self.list_ftp())  - failures) + " files extracted."
        if failures>0:print str(failures) + " expected CSV files could not be found. Try first downloading if you have used the -t option."
