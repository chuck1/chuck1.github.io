from pprint import pprint

repos = [
        'async_patterns',
        'modconf',
        'codemach',
        'ws_storage',
        'ws_sheets',
        'ws_sheets_server',
        'ws_web_aiohttp']

def gen_header():
    yield [
            '',
            ]
    yield [
            '',
            ]
    yield [
            'master',
            ]
    yield [
            'dev',
            ]

def _gen_cols():
    yield [
            '{}_',
            ]
    yield [
            '|{}_docs_latest|',
            '|{}_pypi|',
            '|{}_pypi_versions|',
            ]
    yield [
            '|{}_travis_master|',
            '|{}_codecov_master|',
            ]
    yield [
            '|{}_travis_dev|',
            '|{}_codecov_dev|',
            ]

length = 0

def _format(f, s):
    global length
    s = f.format(s)
    length = max(length, len(s))
    return s

def gen_cols(s):
    for l in _gen_cols():
        yield [_format(_, s) for _ in l]

def gen_rows(repos):
    yield list(gen_header())
    for s in repos:
        yield list(gen_cols(s))

rows = list(gen_rows(repos))

fmt = '{:' + str(length) + '}'

for cols in rows:
    row_sep = '+'
    for _ in cols:
        row_sep += '-' + '-' * length + '-+'
    
    blank = '| '
    for _ in cols:
        blank += fmt.format('') + ' | '
    
    break

# print table

def print_table(prnt):
    prnt(row_sep)
    
    for cols in rows:
    
        while True:
            brk = True
            line = '| '
            for c in cols:
                if c:
                    s = c.pop(0)
                else:
                    s = ''
                if c:
                    brk = False
                line += fmt.format(s) + ' | '
            
            prnt(line)
    
            prnt(blank)
                
            if brk: break
         
        prnt(row_sep)


class Image:
    def __init__(self, s, alias, url, target):
        self.alias = alias.format(s)
        self.url = url.format(s)
        self.target = target.format(s)

    def print_(self):
        return '.. |{}| image:: {}\n   :target: {}'.format(
                self.alias,
                self.url,
                self.target,
                )

def gen_images(repos):
    for s in repos:
        yield Image(
                s,
                '{}_pypi',
                'https://img.shields.io/pypi/v/{}.svg',
                'https://pypi.python.org/pypi/{}',
                )
        yield Image(
                s,
                '{}_pypi_versions',
                'https://img.shields.io/pypi/pyversions/{}.svg',
                'https://pypi.python.org/pypi/{}',
                )
        yield Image(
                s,
                '{}_docs_latest',
                'https://readthedocs.org/projects/{}/badge/?version=latest',
                'https://{}.readthedocs.io/en/latest',
                )
        yield Image(
                s,
                '{}_travis_master',
                'https://travis-ci.org/chuck1/{}.svg?branch=master',
                'https://travis-ci.org/chuck1/{}',
                )
        yield Image(
                s,
                '{}_travis_dev',
                'https://travis-ci.org/chuck1/{}.svg?branch=dev',
                'https://travis-ci.org/chuck1/{}',
                )
        yield Image(
                s,
                '{}_codecov_master',
                'https://codecov.io/gh/chuck1/{}/branch/master/graph/badge.svg',
                'https://codecov.io/gh/chuck1/{}',
                )
        yield Image(
                s,
                '{}_codecov_dev',
                'https://codecov.io/gh/chuck1/{}/branch/dev/graph/badge.svg',
                'https://codecov.io/gh/chuck1/{}',
                )

def gen_links(repos):
    for r in repos:
        yield '.. _{0}: https://github.com/chuck1/{0}'.format(r)

def print_all(prnt):

    print_table(prnt)

    for s in gen_links(repos):
        prnt()
        prnt(s)
    
    for i in gen_images(repos):
        prnt()
        prnt(i.print_())


with open('README.rst', 'w') as f:
    def prnt(s=''):
        f.write(s+'\n')
    print_all(prnt)



