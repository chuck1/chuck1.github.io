#!/usr/bin/env python

import jinja2

if __name__ == '__main__':

    pages = [
            {
                'path':'education/bachelors/auto.html',
                'content':'hi!'
                },
            ]
    
    temp = jinja2.Template(open("base.html.in", "r").read())

    for p in pages:
           
        output = temp.render({
            'left': 'left!',
            'content': p['content'],
            })
        
        with open(p['path'], 'w') as f:
            f.write(output)

