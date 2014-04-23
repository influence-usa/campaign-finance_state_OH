#!/usr/bin/python

import sys, getopt
from work import OHIO

def main(argv):
   if len(argv)==1:
        argv.append("")
   try:
       opts, args = getopt.getopt(argv,"d:p:t:")
   except getopt.GetoptError:
       print 'run.py -d<download>|-p<print> filter_string'
       sys.exit(2)

   state = OHIO(opts[0][1]) 
   if opts[0][0] == '-p':
       state.print_ftp()
   if opts[0][0] == '-d':
       state.get_ftp()
   if opts[0][0] == '-t':
       state.get_ftp()
       state.extract_json_files()

if __name__ == "__main__":
   main(sys.argv[1:])
