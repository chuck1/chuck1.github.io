#!/usr/bin/env python3
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('folder')
args = parser.parse_args()

folder = args.folder

root, last = os.path.split(folder)

if os.path.exists(folder):
    print('already exists')
    sys.exit(1)

if not os.path.exists(root):
    print('root does not exist')
    sys.exit(1)

print(folder)
print(root)
print(last)

title = last.replace('_',' ')

# create folder
os.makedirs(folder)

# create index
with open(os.path.join(folder, 'index.md') , 'w') as f:
    f.write('---\nlayout: default\ntitle: {0}\n---\n# {0}\n\n'.format(title))


    
