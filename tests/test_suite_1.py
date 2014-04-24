import sys,os
import collections
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import  getopt
from work import Ohio

import unittest

class Ohiotests(unittest.TestCase):

### frame
    def setUp(self):
        self.Ohio = Ohio() 
        self.Ohio.unzipped_dir = '/home/aaron/projects/campaign-finance_state_OH/tests/downloads/unzipped'
        self.Ohio.download_dir = '/home/aaron/projects/campaign-finance_state_OH/tests/downloads'
        self.Ohio.data_dir =  '/home/aaron/projects/campaign-finance_state_OH/tests/data'
        #need to delete all files from testing folders
    def test_ftp_connection(self):
        self.assertTrue(len(self.Ohio.filenames)>100)
    def test_download(self):
        pass
if __name__=='__main__':
    unittest.main(   )
