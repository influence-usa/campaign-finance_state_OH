import sys,os
import collections
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from work import Ohio
import unittest
Ohio = Ohio()
class Ohiotests(unittest.TestCase):

    def setUp(self):
        self.Ohio = Ohio
        self.Ohio.unzipped_dir = '/home/aaron/projects/campaign-finance_state_OH/tests/downloads/unzipped'
        self.Ohio.download_dir = '/home/aaron/projects/campaign-finance_state_OH/tests/downloads'
        self.Ohio.data_dir =  '/home/aaron/projects/campaign-finance_state_OH/tests/data'
  #      #need to delete all files from testing folders
    def test_ftp_connection(self):
        self.assertTrue(len(Ohio.filenames)>20)
    def test_download(self):
        pass
if __name__=='__main__':
    unittest.main(   )
