from ftplib import FTP
import os, sys, os.path
#WARNING THIS WILL TAKE A WHILE TO RUN
ftp = FTP("serproxy.sos.state.oh.us") # no pass
direct  ='/home/aaron/pycon/ohio_down/'
ftp.cwd("/free")
filenames = []
ftp.retrlines('NLST', filenames.append)

for filename in filenames:
    if(".EXE" in filename.upper()):
        local_filename = os.path.join(direct, filename)
        file = open(local_filename, 'wb')
        ftp.retrbinary('RETR '+ filename, file.write)


ftp.close()
