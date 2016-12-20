
import os
import json
import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader("site_generator/templates"))

def dirs_generator(dirs):
    for d in dirs:
        link = os.path.join(d, "index.html")
        yield (d, link)

def gen_page(filename):

    print
    print "filename:", filename
    print os.path.splitext(filename)

    src = os.path.join("site_source", filename)
    dst = os.path.join("site", os.path.splitext(filename)[0] + ".html")
    
    dst_link = os.path.join(os.path.splitext(filename)[0] + ".html")

    with open(src, "r") as f:
        d = json.loads(f.read())
    
    filename_template = "site_generator/templates/" + d["template"] + ".html"
    filename_template = d["template"] + ".html"
    #with open(, "r") as f:
    template = env.get_template(filename_template)
    
    dirs = list(os.walk(os.path.dirname(src)))[0][1]
    
    dirs2 = list(dirs_generator(dirs))

    print "dirs:", dirs

    print "d:",repr(d)
    
    context = {
            "title": d["title"],
            "l": dirs2,
            }

    html = template.render(context)

    with open(dst, "w") as f:
        f.write(html)
    
    for d in dirs:
        gen_page(os.path.join(d, "index.txt"))

gen_page("index.txt")


