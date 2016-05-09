#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# requires  pygments-markdown-lexer  for markdown code highlighting

AUTHOR = 'William Minchin'
SITENAME = 'Introduction to Pelican'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['.']
STATIC_PATHS = ['images', 'webpages', 'theme/fonts', 'css', ]

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'

READERS = {'html': None,
           'htm': None}

#THEME = '../pelican-themes/pelican-bootstrap3'
THEME = '../minchinweb.github.io-pelican/themes/pelican-minchin-ca'
BOOTSTRAP_THEME = 'flatly'
#SITELOGO = 'images/pelican-logo.png'
SITELOGO_SIZE = '25px'
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
#BOOTSTRAP_NAVBAR_INVERSE = True

CUSTOM_CSS_LIST = ['theme/css/typogrify.css',
                   'theme/css/font-awesome.min.css',
                   'theme/css/pygments/solarizeddark.css',
                   'css/intro-to-pelican.css',
                  ]


DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_URL =              '{slug}/'
PAGE_SAVE_AS =          '{slug}/index.html'

ARCHIVES_URL =          ''
ARCHIVES_SAVE_AS =      ''

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# Plugins
PLUGIN_PATHS = ['../pelican-plugins', ]
#PLUGINS = ['tipue_search', ]
PLUGINS = ['assets', ]

ASSET_CSS = False
ASSET_JS = False

MD_EXTENSIONS = ['markdown.extensions.extra',
                 'codehilite(css_class = highlight, linenums = True)',
                 'pymdownx.superfences',
                 ]


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-384291-3'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'minchin.ca'

# # Make things disappear
DISPLAY_CATEGORIES_ON_MENU = False
#HIDE_SITENAME = True
HIDE_SIDEBAR = True
FEED_ALL_ATOM = False
FEED_ALL_RSS = False
GITHUB_USER = False
ADDTHIS_PROFILE = False
DISQUS_SITENAME = False
PDF_PROCESSOR = False
