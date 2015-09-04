
import re

def proc0(s):
    #p ='([^ ]+)'
    p  = '(\d+)\.(\d+)\.(\d+)\.(\d+)'
    p += ' [^ ]+ [^ ]+ '
    p += '\[(\d+/\w+/\d+)(:\d\d:\d\d:\d\d).*\] "([^"]+)" .*'
    
    m = re.match(p, s)
    if m:
        print m.group(1)
        print m.group(2)
        print m.group(3)
        print m.group(4)
        print m.group(5)
        print m.group(6)
        return "{:>2}.{:>2}.{:>2}.{:>2}".format(
                hex(int(m.group(1))).upper()[2:],
                hex(int(m.group(2))).upper()[2:],
                hex(int(m.group(3))).upper()[2:],
                hex(int(m.group(4))).upper()[2:],
                )


with open('/var/log/apache2/access.log', 'r') as f:
    t = f.read()

print len(t)

lines = t.split('\n')

print len(lines)

lines = list(proc0(l) for l in lines)
lines = list(l for l in lines if l)

from itertools import groupby

lines1 = [(key,len(list(group))) for key, group in groupby(lines)]

print len(lines1)


for k,l in lines1:
    print l,k
    pass


