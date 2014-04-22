import config
from ftplib import FTP
import os, sys, os.path
import re
#WARNING THIS WILL TAKE A WHILE TO RUN
class OHIO(object):
    def __init__(self): 
        self.ftp = FTP("serproxy.sos.state.oh.us") # no pass
        self.ftp.login()
        self.ftp.cwd("/free")
        self.filenames = []
        self.ftp.retrlines('NLST', self.filenames.append)
    def __del__(self):
        self.ftp.close()
        print "OHIO ftp closed"

    def print_ftp(self,filter=None):
        for filename in self.list_ftp(filter):
            print filename

    def download_ftp(self,filter=None):
        for filename in self.list_ftp(filter):
            local_filename = os.path.join( config.download_dir, filename)
            file = open(local_filename, 'wb')
            self.ftp.retrbinary('RETR '+ filename, file.write)
   
    def list_ftp(self,filter=''):
        str = '.*' + filter  + '.*\\.EXE'
        regex = re.compile(str)
        for filename in self.filenames:
            if re.match(regex, filename.upper()):
                yield filename  



