import os
import json
from pprint import pprint

import pymongo
import pygraphviz
import crayons

client = pymongo.MongoClient(os.environ['MONGO_URI'])

db = client['literature']

def makedirs(d):
    try:
        os.makedirs(d)
    except:
        pass

def generate_pages():
    for a in db.articles.find():

        dst = os.path.join('pages/literature/articles', str(a['_id']) + '.md')
        
        makedirs(os.path.dirname(dst))

        with open(dst, 'w') as f:
            f.write('---\nlayout: default\n---\n\n')

            f.write('## id\n\n{}\n\n'.format(str(a['_id'])))
            f.write('## title\n\n{}\n\n'.format(a['title']))
            f.write('## notes\n\n{}\n\n'.format(a.get('notes','')))
            f.write('## year\n\n{}\n\n'.format(a.get('year','')))

            f.write('## authors\n\n')

            for a_id in a['authors']:
                author = db.authors.find_one({'_id': a_id})
                
                link = '/pages/literature/authors/{}.html'.format(str(a_id))

                f.write(' * [{}]({})'.format(author['name'], link))

if __name__ == '__main__':
    generate_pages()

