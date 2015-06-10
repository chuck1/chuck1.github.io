#!/usr/bin/env python

import os
import json
import jinja2

class Course:
    pass

def d2c(d):
    c = Course()
    c.__dict__ = d
    return c

def gen(d):
    fn = os.path.join(d,'index.html.in')
    temp = jinja2.Template(open(fn,'r').read())
    
    fn = os.path.join(d,'courses.json')
    with open(fn, 'r') as f:
        cs1 = json.load(f)
    
    cs2 = list(d2c(c) for c in cs1)
    
    s = temp.render(
            courses_mth = filter(lambda c: c.subject == 'MTH', cs2),
            courses_ch  = filter(lambda c: c.subject == 'CH', cs2),
            courses_me  = filter(lambda c: (c.subject == 'ME') and (not('thesis' in c.desc)) and (not('sem/' in c.desc)), cs2),
            courses_cs  = filter(lambda c: (c.subject == 'CS'), cs2),
            )

    #print s

    fn = os.path.join(d,'index.html')
    with open(fn, 'w') as f:
        f.write(s)


if __name__ == '__main__':
    gen('bachelors')
    gen('masters')

