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
        self.allfiles = []
        try:
            self.ftp = FTP("serproxy.sos.state.oh.us") # no pass
            self.ftp.login()
            self.ftp.cwd("/free")
            self.ftp.retrlines('NLST', self.allfiles.append)
        except:
            print "ftp was not connected"
        #I need to find out exactly what fies are needed
        regex = re.compile('(?=ALL.*(19|20)\d{2})(?=.*(^(?!.*?MSTRKEY)))')
        self.filenames =  [x for x in self.allfiles if (regex.search(x.upper()) is not None)]
        self.unzipped_dir = config.unzipped_dir
        self.data_dir = config.data_dir
        self.download_dir = config.download_dir

    def __del__(self):
        self.ftp.close()
        print "OHIO ftp closed"

    def set_up_directories(self):
        for d in ["CAN","PAR","PAC"]:
            if  d not in  [name for name in os.listdir(self.data_dir)]:
                os.makedirs(self.data_dir  + "/" + d)
                os.makedirs(self.data_dir  + "/" + d + "/CON" )
                os.makedirs(self.data_dir  + "/" +  d + "/EXP")
             
    def print_ftp(self):
        for files in self.list_ftp():
            print files[0] + " - FileSize:" + str(files[1])

    def report(self):
        for filename in self.list_ftp():
            filename_str = filename[0].replace(".EXE",".CSV")
            file_name_parts = filename_str.split("_") 
            data_base_dir = self.data_dir + "/" + file_name_parts[1] + "/" + file_name_parts[2] + "/" + file_name_parts[3][:4]
            print filename[0][:-4] 
            for  direct in os.walk(data_base_dir).next()[1]:
                files = os.walk(data_base_dir + "/" + direct).next()[2]
                print " ------------- "  + direct + ": " +  str(len(files)) + " files"
            
        
            
    def download_ftp(self):
        self.set_up_directories()
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

    def get_date(self,date_str):
        if (date_str is None)or(date_str == ""): return False
        try:
            dt = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S')
        except:
            return False
        return dt    

    def get_quarter(self,date_str):
        dt = self.get_date(date_str)
        q_gen = [ [i+1,x] for i,j in enumerate([1, 4, 7,10] )for x in range(j,j+3)] 
        for x in q_gen:
            if dt.date().month == x[1]:
                return x[0]
        return False           

    def get_file_date_field(self,file_name): 
        types ={'ALL_CAN_CON':'CANCONT_DATE','ALL_CAN_EXP':'CANEXPEND_DATE','ALL_PAC_CON':'PACCONT_DATE','ALL_PAC_EXP':'PACEXPEND_DATE',
                'ALL_PAR_CON':'PARTYCONT_DATE','ALL_PAR_EXP':'PARTYEXPEND_DATE'}
        for key in types:
            if key in file_name: 
                return types[key]
        return False
    def extract_json_files(self):
         #SEE LATIN1 BELOW! Change this depending on the data
        failures = 0    
        print  "extracting " + str(sum(1 for x in self.list_ftp())) +  " csv files to json"
        for filename in self.list_ftp():

            filename_str = filename[0].replace(".EXE",".CSV")
            try:
                input_file = unicodecsv.DictReader(open(config.unzipped_dir + "/" + filename_str), encoding='latin1')
            except:
                print  filename_str  + " from the ftp site does not exist in your local directories so json extraction is skipped for " + filename + "."
                input_file =  ""
                failures += 1

            date_field = self.get_file_date_field(filename_str)
            bad_date_num = 0
            for (x, d) in enumerate(input_file):
                d['id']=x
                Q = 'BAD_DATE' 
                if date_field not in d:
                   bad_date_num +=  1
                elif self.get_date(d[date_field]) == False:
                   bad_date_num +=  1
                else:
                    Q = "Q" + str(self.get_quarter(d[date_field]))

                file_name_parts = filename_str.split("_") 
                data_base_dir = self.data_dir + "/" + file_name_parts[1] + "/" + file_name_parts[2] + "/" + file_name_parts[3][:4]
                if not os.path.exists(data_base_dir ):
                    os.makedirs(data_base_dir)
                    for i in range(1, 5):
                        if not os.path.exists(data_base_dir + "/Q" + str(i)):os.makedirs(data_base_dir + "/Q" + str(i))

                if not os.path.exists(data_base_dir + "/BAD_DATE" ):os.makedirs(data_base_dir + "/BAD_DATE" )

                with open( data_base_dir + "/" + Q + "/" +  str(d['id']) + '.json', 'w') as outfile:
                    json.dump(d, outfile)
            if bad_date_num > 0:print str(bad_date_num) + " bad dates were found in " + filename_str
        print str(sum(1 for x in self.list_ftp())  - failures) + " files extracted."
        if failures>0:print str(failures) + " expected CSV files could not be found. Try first downloading if you have used the -t option."
