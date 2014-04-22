#!/usr/bin/python

import sys, getopt
from download import OHIO

def main(argv):
   state = OHIO() 
   if len(argv)==1:
        argv.append("")
   try:
       opts, args = getopt.getopt(argv,"d:p:")
   except getopt.GetoptError:
       print 'run.py -d<download>|-p<print> filter_string'
       sys.exit(2)
   if opts[0][0] == '-p':
       state.print_ftp(filter=opts[0][1])
   if opts[0][0] == '-d':
       state.download_ftp(filter=opts[0][1])


if __name__ == "__main__":
   main(sys.argv[1:])
