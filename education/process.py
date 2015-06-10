#!/usr/bin/env python

import os
import re
import json

def process(directory):

    with open(os.path.join(directory,'courses.txt'),'r') as f:
        lines = f.readlines()
    
    lst = []
    
    for line in lines:
        m = re.match("^(\w+)\s+(\d+)\s+(\w+)\s+(\*?\w+.*)", line)
        
        #print repr(m.group(1))
        #print repr(m.group(2))
        #print repr(m.group(3))
        #print repr(m.group(4))
    
        d = {
                "subject":m.group(1),
                "number": m.group(2),
                "desc":   m.group(4).lower(),
                }
    
        lst.append(d)
    
    print lst
    
    s = json.dumps(lst)
    
    with open(os.path.join(directory,'courses.json'),'w') as f:
        f.write(s)
   
if __name__ == '__main__':
    process('bachelors')
    process('masters')

