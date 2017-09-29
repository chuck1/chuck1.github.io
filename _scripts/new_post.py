#!/usr/bin/env python3
import sys
import os
import datetime
import pytz

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('title')
args = parser.parse_args()

tz = pytz.timezone('US/Pacific')

now = datetime.datetime.now()
now = tz.localize(now)

title = args.title.lower()
title_safe = args.title.replace(' ','-')

dt1 = now.strftime('%Y-%m-%d-%H%M%S%z')

dt = now.strftime('%Y-%m-%d %H:%M:%S %z')

s = dt1 + '-{}.md'.format(title_safe)

print(now)


print(s)

dst = os.path.join('_posts', s)

if os.path.exists(dst):
    print('file already exists')
    sys.exit(1)

with open(dst, 'w') as f:
    f.write('---\n')
    f.write('layout: default\n')
    f.write('date: {}\n'.format(dt))
    f.write('title: {}\n'.format(title))
    f.write('---\n\n')


