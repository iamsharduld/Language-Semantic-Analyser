
'''vals = {}

fh = open("new.csv",'r+')
myarr = f
'''

import json


with(open('my_dict.json')) as f:
    my_dict = json.load(f)
c = 0
for i in my_dict:
    print i , my_dict[i]
    c+=1
    if(c == 10):
        break

