import markdown
import os
import json
import jinja2
import resume
import snipets.json_to_object

env = jinja2.Environment(loader=jinja2.FileSystemLoader("site_generator/templates"))

source_dir = "source/site1"

nav = None

def source_to_web(filename):
    return os.path.join("/", os.path.splitext(filename)[0] + ".html")

def resume_to_site_source(filename):
    p = resume.Person()
    p.load(filename)

class Page(object):
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.data = json.loads(f.read())
        
        self.src_relpath = os.path.relpath(filename, source_dir)

        self.filename = filename

        self.text_html = markdown.markdown(self.data["text"])
        try:
            self.text_menu_html = markdown.markdown(self.data["text_menu"])
        except:
            self.text_menu_html = ""

        dirs = list(os.walk(os.path.dirname(filename)))
        dirs = dirs[0][0:2]
        dirs2 = list(dirs_generator(dirs))
    
    def subpages(self):
        dirs = list(os.walk(os.path.dirname(self.filename)))
        dirs = dirs[0][0:2]
        dirs2 = list(dirs_generator(dirs))
        for _,_,_,page in dirs2:
            yield page

    def nav(self):
 
        pages = list(self.subpages())
       
        if pages:
            a_attr = "aria-haspopup=\"true\""
        else:
            a_attr = ""

        html = "<li><a href=\"{0}\" {1}>{0}</a>".format(source_to_web(self.src_relpath), a_attr)
        
        print self.filename
        if pages:
            html += "<ul>"

            for page in pages:
                html += page.nav()

            html += "</ul>"
        
        html += "</li>"

        return html


def dirs_generator(walk):
    d0, dirs = walk

    #print "dirs generator"
    for d in dirs:
        #print "  d0 = {}".format(d0)
        #print "  {}".format(d)

        #filename = os.path.join(source_dir, d, "index.txt")
        filename = os.path.join(d0, d, "index.txt")

        #print "  {}".format(filename)

        page = Page(filename)

        #print "d2:", repr(d2)
        
        link = os.path.join(d, "index.html")

        yield (d, page.text_menu_html, link, page)

def gen_page(filename):

    d0 = os.path.dirname(filename)

    print
    print "filename: ", filename
    print "directory:", d0
    print os.path.splitext(filename)


    src = os.path.join(source_dir, filename)
    dst = os.path.join("site", os.path.splitext(filename)[0] + ".html")
 
    page = Page(src)
   
    dst_link = os.path.join(os.path.splitext(filename)[0] + ".html")

    with open(src, "r") as f:
        d = json.loads(f.read())
    
    filename_template = "site_generator/templates/" + d["template"] + ".html"
    filename_template = d["template"] + ".html"
    #with open(, "r") as f:
    template = env.get_template(filename_template)
    
    dirs = list(os.walk(os.path.dirname(src)))

    print "dirs"
    for x in dirs:
        print "  ",x
    
    dirs = dirs[0][0:2]
 
    print "dirs", dirs

    dirs2 = list(dirs_generator(dirs))

    print "dirs:", dirs

    
    text = d["text"]
    
    print "text:", repr(text)
    text_html = repr(markdown.markdown(text))
    print "text html:", text_html
    
    context = {
            "title": d["title"],
            "l": dirs2,
            "nav": nav,
            }

    html = template.render(context)
    
    try:
        os.mkdir(os.path.dirname(dst))
    except: pass

    with open(dst, "w") as f:
        f.write(html)
    
    for d1 in dirs[1]:
        print "d0=",d0
        print "d1=",d1
        gen_page(os.path.join(d0, d1, "index.txt"))

    return page

##################################33

page = Page(os.path.join(source_dir, "index.txt"))

nav = page.nav()




gen_page("index.txt")


#resume_to_site_source("/home/crymal/backedup/git/personal/resume.txt")







