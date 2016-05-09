title: Genealogy Configuration

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys
sys.path.append(os.curdir)

# Adam configuration options
ADAM_PUBLISH = False
from adamconf import *
# ADAM = True  is used by the theme tempates to display 'Genealogy only' things

AUTHOR = 'D. Minchin & Wm. Minchin'
SITENAME = 'Minchin.ca'
#SITEURL = 'http://minchin.ca/genealogy'
if ADAM_PUBLISH:
    SITEURL = 'http://minchin.ca/genealogy'
    RELATIVE_URLS = False
else:
    SITEURL = '.'
    # Uncomment following line if you want document-relative URLs when developing
    RELATIVE_URLS = True
SITE_ROOT_URL = 'http://minchin.ca'

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# static paths will be copied under the same name
# these are relative to the base CONTENT folder
STATIC_PATHS = ['images',
                '../extras',
                'css',
                'design',
                'js',
                'pages/img',
                '../.gitattributes',
                '../.gitignore',
                '../README.txt',
                ]

# A list of files to copy from the source to the destination
EXTRA_PATH_METADATA = {
    '../.gitattributes':            {'path': '.gitattributes'},
    '../.gitignore':                {'path': '.gitignore'},
    '../README.txt':                {'path': 'README.txt'},
    '../extras/minchin.ico':        {'path': 'favicon.ico'},
    '../extras/.nojekyll':          {'path': '.nojekyll'},
    'js/tab-list-handler.js':       {'path': 'tab-list-handler.js'},
    'js/tooltip-handler.js':        {'path': 'tooltip-handler.js'},
    'js/graph-handler.js':          {'path': 'graph-handler.js'},
    'js/gigatrees-map-min.js':      {'path': 'gigatrees-map-min.js'},
    'pages/img/arrowd.png':         {'path': 'arrowd.png'},
    'pages/img/arrowl.png':         {'path': 'arrowl.png'},
    'pages/img/arrowr.png':         {'path': 'arrowr.png'},
    'pages/img/arrowu.png':         {'path': 'arrowu.png'},
    'pages/img/bg-black.png':       {'path': 'bg-black.png'},
    'pages/img/bg-pattern.png':     {'path': 'bg-pattern.png'},
    'pages/img/mapicon_f.png':      {'path': 'mapicon_f.png'},
    'pages/img/mapicon_m.png':      {'path': 'mapicon_m.png'},
    'pages/img/mapicon_u.png':      {'path': 'mapicon_u.png'},
    'pages/img/mapmarker1.png':     {'path': 'mapmarker1.png'},
    'pages/img/mapmarker2.png':     {'path': 'mapmarker2.png'},
    'pages/img/mapmarker3.png':     {'path': 'mapmarker3.png'},
    'pages/img/mapmarker4.png':     {'path': 'mapmarker4.png'},
    'pages/img/mapmarker5.png':     {'path': 'mapmarker5.png'},
    'pages/img/avatar.jpg':         {'path': 'avatar.jpg'},
    'pages/img/image.jpg':          {'path': 'image.jpg'},
    'pages/img/pdf.jpg':            {'path': 'pdf.jpg'},
    }


# Custom settings
#FILENAME_METADATA = ('(?P<date>\d{4}-\d{2}-\d{2}).*')  # default?
#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'  # extract date and slug
FILENAME_METADATA = '(?P<slug>[\w-]*)'      # so anything before the file extension becomes the slug
## Please note that the metadata available inside your files takes precedence
#  over the metadata extracted from the filename.

MARKUP = (('rst',
           'md',
           'markdown',
           'mkd',
           'mdown',
           'html',
           'htm'))
PATH = 'content'
OUTPUT_PATH = '../genealogy-gh-pages/'

# Add Blog to sidebar
MENUITEMS = (('Blog',        'http://blog.minchin.ca/',      'fa fa-pencil'),
             ('Genealogy',   SITEURL,                        'glyphicon glyphicon-tree-deciduous'),
             ('My Projects', 'http://minchin.ca/projects/',  'fa fa-flask'),
             ('Search',      'http://minchin.ca/search/',    'fa fa-search'),
             ('About',       'http://minchin.ca/about/',     'fa fa-info-circle'),
             ('Contact Me',  'http://minchin.ca/contact/',   'fa fa-envelope'),
             )

MENUITEMS_2_AT = 'Genealogy'
MENUITEMS_2_AT_LINK = ''  # this is added to SITEURL

MENUITEMS_2 = (('Surnames',         SITEURL + '/names.html',          False),
               ('Updates',          SITEURL + '/updates.html',        False),
               ('Sources',          SITEURL + '/sources.html',        False),
               ('Distribution Map', SITEURL + '/map.html',            False),
               ('Timelines',        SITEURL + '/timeline.html',       False),
               #('Immigrants',       SITEURL + '/immigrants.html',     False),  # doens't exist in current builds
               #('Nobility',         SITEURL + '/titles.html',         False),  # doens't exist in current builds
               ('Locations',        SITEURL + '/places.html',         False),
               ('Bonkers Report',   SITEURL + '/bonkers-report.html', False),
               ('Photos',           SITEURL + '/photos.html',         False),
               #('External Links',   SITEURL + '/links.html',          False),  # doens't exist in current builds
               #('Statistics',       SITEURL + '/stats.html',          False),  # stats graphs aren't working right now
               )


DISPLAY_PAGES_ON_MENU = False

# disable Tags, etc
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_URL = ''
CATEGORIES_SAVE_AS = ''
ARTICLE_URL = ''
ARTICLE_SAVE_AS = ''
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_URL = ''
ARCHIVES_SAVE_AS = ''
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

# Theme Related
TYPOGRIFY = False  # turn off for HIDDEN names...
THEME = '../minchinweb.github.io-pelican/themes/pelican-minchin-ca'
SITELOGO = 'images/MinchindotCA-200.png'
SITELOGO_SIZE = '100%'
PYGMENTS_STYLE = 'friendly'
DISPLAY_BREADCRUMBS = True
FAVICON = 'favicon.ico'
BOOTSTRAP_THEME = 'minchin-ca'
USE_OPEN_GRAPH = True
CUSTOM_CSS = 'css/minchin-ca.css'
DOCUTIL_CSS = False
CUSTOM_JS_LIST = ['js/jquery-ui.min.js',
                  'js/globalize.min.js',
                  'js/dx.chartjs.js',
                  ]

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-384291-3'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'minchin.ca'

# Plugins
#PLUGIN_PATH = '../pelican-plugins'
PLUGIN_PATHS = ('../pelican-plugins',)
# PLUGINS = ['assets', 'minify', 'sitemap', 'optimize_images']
PLUGINS = ['assets', ]

ASSET_CSS = False
ASSET_JS = False

SITEMAP = {
    "format": "xml",
}

# `assets` sounds good, but I can't figure out how to get it to work for my CSS
# `better_figures_and_images` didn't seem to do what I wanted (see Projects)
# `gallery` looks good, but don't have a use here yet
# `liquid_tags` & `pelican_comment_system` might be useful...
# `optimize_images` works, but I don't have many images yet
#       - requires `jpegtran.exe` <http://jpegclub.org/jpegtran/> and
#           `optinpng.exe` <http://sourceforge.net/projects/optipng/>
# look into 'neighbors' plugin for profiles


# # Make things disappear
DISPLAY_CATEGORIES_ON_MENU = False
HIDE_SITENAME = True
HIDE_SIDEBAR = True
FEED_ALL_ATOM = False
FEED_ALL_RSS = False
GITHUB_USER = False
ADDTHIS_PROFILE = False
DISQUS_SITENAME = False
PDF_PROCESSOR = False
```

### adamconf.py

```python
# Genealogy Uploader, v.3.2.3
# C:\Users\William\Desktop\William 160108.ged

ADAM = True
ADAM_VERSION = "Built by Gigatrees (3.0.14)"
ADAM_UPDATED = "January 8, 2016"
ADAM_COPY_DATE = "1987-2016"
ADAM_LINK = "http://gigatrees.com"
ADAM_FOOTER = "<p><strong>Are we related?</strong> Are you a long lost cousin? Spotted an error here? This website remains a work-in-progress and I would love to hear from you. Drop me a line at minchinweb [at] gmail [dot] com.</p>"
ADAM_PUBLISH = True
```
