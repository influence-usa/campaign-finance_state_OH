# -*- coding: utf-8 -*-

import json
import unicodecsv

#SEE LATIN1 BELOW! Change this depending on the data
input_file = unicodecsv.DictReader(open("/home/aaron/pycon/ohio_down/test/All_CAN.csv"), encoding='latin1')

lst = []

for (x, d) in enumerate(input_file):
    d['id']=x
    lst.append(d)

for d in lst:
    with open('/home/aaron/pycon/ohio_down/json_files/' + str(d['id']) + '.json', 'w') as outfile:
        json.dump(d, outfile)
