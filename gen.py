#!/usr/bin/env python

import jinja2
import json

import myos.path

if __name__ == '__main__':


    pages = json.load(open("data.json","r"))

    temp = jinja2.Template(open("base.html.in", "r").read())

    paths = []

    for p in pages:
           
        paths.append(myos.path.pathlist(p['path']))

        output = temp.render({
            'left': 'left!',
            'content': p['content'],
            })
        
        with open(p['path'], 'w') as f:
            f.write(output)


    print "paths"
    print paths

