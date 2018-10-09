#!/Users/chuanqi/anaconda3/bin/python

import sys
import json

j=json.load(open('small_sample.json'))
jj=j['results']
jjj = {k:jj[k] for k in list(jj.keys())[:int(sys.argv[1])]}
j['results']=jjj
with open('tiny_sample.json', 'w') as outfile:
    json.dump(j, outfile)
