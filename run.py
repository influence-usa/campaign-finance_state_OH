#!/usr/bin/python

import os
import sys, getopt

def main(argv):
   if len(argv)==1:
        argv.append("")
   try:
       opts, args = getopt.getopt(argv,"d:p:j:t")
   except getopt.GetoptError:
       print 'run.py -d<download>|-p<print> filter_string'
       sys.exit(2)

   if opts[0][0] in ['-p','-d','-j']:
       from work import Ohio
       state = Ohio(opts[0][1]) 
       if opts[0][0] == '-p':
           state.print_ftp()
       if opts[0][0] == '-d':
           state.get_ftp()
       if opts[0][0] == '-j':
           state.extract_json_files()

   if opts[0][0] == '-t':
        os.system("python tests/test_suite_1.py")
        
if __name__ == "__main__":
   main(sys.argv[1:])
