title: JRNL Configuration

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import re

import prjct
# requires  pymdown-extensions

AUTHOR = u'WM'
SITENAME = u'Jrnl Notebook'
SITEURL = ''

PATH = 'content'
CUSTOM_CSS = SITEURL + '_css/jrnl.css'

CACHE_CONTENT = True
LOAD_CACHE_CONTENT = True
CHECK_MODIFIED_METHOD = 'md5'   # default is the file's modified time, which is
                                # useless for us because we keep regenerating
                                # the source files

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = ['code', 'pre', 'tt']

STATIC_PATHS = ['images', '_css']

THEME = 'themes/pelican-bootstrap3'

FAVICON = SITEURL + 'images/favicon.ico'
FAVICON_IE = SITEURL + 'images/favicon.ico'
SITELOGO = SITEURL + 'images/favicon-48.png'

ELEVATOR = False

BOOTSTRAP_THEME = 'superhero'
USE_PAGER = True
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_TAGS_INLINE = True
DISPLAY_BREADCRUMBS = True

MD_EXTENSIONS = [#'fenced_code',                         # fenced_code allows using three backticks to notate code
                                                        # see https://github.com/getpelican/pelican/issues/1238
                 'pymdownx.superfences',                # https://facelessuser.github.io/pymdown-extensions/extensions/superfences/
                 'codehilite(css_class=highlight)',     # set linenums=True for line numbers
                                                        # https://pythonhosted.org/Markdown/extensions/code_hilite.html
                 'pymdownx.caret',                      # use single caret for superscript
                                                        # use double caret for insertion (underline?)
                                                        # https://facelessuser.github.io/pymdown-extensions/extensions/caret/
                 'pymdownx.tilde',                      # use single tildes for subscript
                                                        # use double tildes for deletion
                                                        # https://facelessuser.github.io/pymdown-extensions/extensions/tilde/
                 'pymdownx.tasklist',                   # GitHub style task lists for `- [ ] task`
                 'markdown.extensions.extra',           # on by default
                                                        # see https://pythonhosted.org/Markdown/extensions/extra.html
                 'markdown.extensions.smarty',          # https://pythonhosted.org/Markdown/extensions/smarty.html         
                 ]
# progress bars -- https://facelessuser.github.io/pymdown-extensions/extensions/progressbar/
# githubemoji -- https://facelessuser.github.io/pymdown-extensions/extensions/githubemoji/
# SmartSymbols -- Auto-convert special symbols, like (tm) to ™ -- https://facelessuser.github.io/pymdown-extensions/extensions/smartsymbols/
# Admonition -- https://pythonhosted.org/Markdown/extensions/admonition.html
# Tweetable Links -- https://github.com/max-arnold/markdown-tweetable
# general comments -- see https://github.com/getpelican/pelican/wiki/Tips-n-Tricks#custom-markdown-extensions
# HTML5 pictures -- https://github.com/speechkey/mdx_picture


# A list of metadata fields containing reST/Markdown content to be parsed and translated to HTML.
FORMATTED_FIELDS = ['title', 'summary']

PLUGIN_PATHS = ['../GitHub/pelican-plugins', ]
PLUGINS = ['tipue_search',
           'tag_cloud',
           'prjct.titlecase',  # titlecase Jinja filter
           ]

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

prjct_release = str(prjct.__version__)
p = re.compile('\d+\.\d+(\.\d+)?')
prjct_versionmatch = p.match(prjct_release)
prjct_version = prjct_versionmatch.group()

PRJCT = True
PRJCT_TODO, PRJCT_DONE = prjct.todo_export.to_html_dicts(prjct.config.load())
PRJCT_PROJECTS = prjct.todo_export.project_list()
PRJCT_DESC = prjct.descriptions.to_html_dict(prjct.config.load(), MD_EXTENSIONS)
PRJCT_VERSION = prjct_version
PRJCT_URL = prjct.__url__


PAGE_URL =              '{slug}/'
PAGE_SAVE_AS =          '{slug}/index.html'
TAGS_URL =              'tags/'
TAGS_SAVE_AS =          'tags/index.html'
TAG_URL =               'tags/{slug}/'
TAG_SAVE_AS =           'tags/{slug}/index.html'
CATEGORIES_URL =        'categories/'
CATEGORIES_SAVE_AS =    'categories/index.html'
CATEGORY_URL =          'categories/{slug}/'
CATEGORY_SAVE_AS =      'categories/{slug}/index.html'
AUTHORS_URL =           'authors/'
AUTHORS_SAVE_AS =       'authors/index.html'
AUTHOR_URL =            'authors/{slug}/'
AUTHOR_SAVE_AS =        'authors/{slug}/index.html'

# {date:%b}  gives short month in words (i.e. 'Apr')
ARTICLE_URL =           'posts/{date:%Y}/{date:%-m}/{date:%-d}/{slug}/'
ARTICLE_SAVE_AS =       'posts/{date:%Y}/{date:%-m}/{date:%-d}/{slug}/index.html'
DAY_ARCHIVE_URL =       'posts/{date:%Y}/{date:%-m}/{date:%-d}/'
DAY_ARCHIVE_SAVE_AS =   'posts/{date:%Y}/{date:%-m}/{date:%-d}/index.html'
MONTH_ARCHIVE_URL =     'posts/{date:%Y}/{date:%-m}/'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%-m}/index.html'
YEAR_ARCHIVE_URL =      'posts/{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS =  'posts/{date:%Y}/index.html'

ARCHIVES_URL =          'posts/'
ARCHIVES_SAVE_AS =      'posts/index.html'

PRJCT_URL =             'prjct/'
PRJCT_SAVE_AS =         'prjct/index.html'


DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 
                    'search', 'tags', '404', 'prjct']
PAGINATED_DIRECT_TEMPLATES = ['index', 'archives']
```