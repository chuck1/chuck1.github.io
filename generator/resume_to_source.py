

import argparse
import json
import os

def clean(s):
    s = s.replace(' ','_')
    s = s.lower()
    return s

###########################################

parser = argparse.ArgumentParser()
parser.add_argument("FILE")

args = parser.parse_args()

src_dir = os.path.dirname(args.FILE)

with open(args.FILE, 'r') as f:
    data = json.loads(f.read())

work = sorted(data['work'], cmp=lambda x,y: cmp(x['start_date'], y['start_date']), reverse=True)

print repr(data)
print
print repr(data["work"])
print

for w in work:
   
    dst_dir = os.path.join("source","site1","work",clean(w['company']))

    print "work data"
    print "save to:", dst_dir

    print repr(w)
    print

    # create page data
    
    page_data = dict()
    
    page_data['template']='page1'
    page_data['title']=w['company']
    page_data['text_menu_1']=w['company']
    page_data['text_menu_2']=w['company']
    page_data['text']={'link':'index_text.txt'}

    try:
        os.makedirs(dst_dir)
    except: pass

    with open(os.path.join(dst_dir, 'index.txt'), 'w') as f:
        f.write(json.dumps(page_data))
    
    with open(os.path.join(src_dir, w['text']['link']), 'r') as f:
        text = f.read()

    with open(os.path.join(dst_dir, 'index_text.txt'), 'w') as f:
        f.write(text)
  

    print repr(page_data)
    print

"""
{
"template":"page1",
"title": "Nortek Air Solutions",
"text_menu_1": "Nortek Air Solutions",
"text_menu_2": "Nortek Air Solutions",
"text": ""
}
"""

