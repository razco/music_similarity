'''
Created on Jun 3, 2017

@author: Raz
'''
import json
from pprint import pprint
with open('AUD_DW0146.json') as data_file:
    data = json.load(data_file)
pprint(data)

print 'gaga'