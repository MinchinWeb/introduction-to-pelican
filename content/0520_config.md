title: Burst Energy Configuration

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Burst Energy'
SITENAME = 'Burst Energy'
SITEURL = 'https://www.burstenergy.ca'    # used by the sitemap generator
WEB_URL = ''    # "SITEURL" as used by the templates (so for the published web pages)
CANONICAL_SITEURL = SITEURL

PATH = 'content'
OUTPUT_PATH = 'output'

TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = 'theme/burst-energy'
CUSTOM_CSS = 'css/burst-energy.css'
BANNER_SUBTITLE = 'Simple Electricity'
HIDE_SIDEBAR = True
BANNER = BANNER_ALL_PAGES = False
TYPOGRIFY = True
COPY_DATE = '2014-15'
BOOTSTRAP_NAVBAR_INVERSE = False
SITELOGO = WEB_URL + 'images/burst-energy-logo-sol-white-230.png'
# SITELOGO_WIDTH = '110px'
SITELOGO_HEIGHT = '25px'
FOOTER_LOGO = WEB_URL + 'images/burst-energy-logo-sol-230.png'
FOOTER_LOGO_WIDTH = '220px'
HIDE_SITENAME = True
BOOTSTRAP_THEME = 'burst-energy'
# BOOTSTRAP_THEME = 'flatly'
THEME_COLOR = "#2C3E50"

FAVICON = WEB_URL + 'images/favicon.png'
FAVICON_IE = WEB_URL + 'favicon.ico'
TOUCHICON = WEB_URL + 'images/apple-touch-icon.png'
# PYGMENTS_STYLE =

GOOGLE_ANALYTICS_UNIVERSAL = 'UA-49197109-1'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'burstenergy.ca'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVES_ON_MENU = False
MENU_ITEMS_ONE = (('News', WEB_URL + '/news/', None),
                  ('Our Rates', WEB_URL + '/rates/', None),
                  ('Electricity 101', WEB_URL + '/electricity-101/', None),
                  )
MENU_ITEMS_TWO = (('Sign Up', WEB_URL + '/mysecure/signup.html', 'glyphicon glyphicon-ok-circle'),
                  ('My Account', WEB_URL + '/mysecure/portal.html', 'fa fa-sign-in'),
                  )
INDEX_SAVE_AS = "news/index.html"
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Link Structure
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'news/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'news/{date:%Y}/index.html'
CATEGORIES_SAVE_AS = 'category/index.html'
AUTHORS_SAVE_AS = 'author/index.html'

STATIC_PATHS = ['images',
                'js',
                'favicon.ico',
                'browserconfig.xml',
                'robots.txt', ]

# Contact Info
CONTACT_WEB_EMAIL = "webteam@burstenergy.ca"
CONTACT_PHONE = "(780) 665-9918"
C_RETAIL_FAX = "(403) 265-7290"
C_CORPORATE_EMAIL = "william@burstenergy.ca"
FOOTER_ADDRESS = "Suite 200, 1316 9<sup>th</sup> Avenue SE<br />Calgary, Alberta T2G&nbsp;0T3"
SOCIAL = (('facebook', 'https://www.facebook.com/BurstEnergyCA'),
          ('twitter', 'http://twitter.com/BurstEnergy'),
          )
FOOTER_LINKS = (('About Us',    WEB_URL + '/about/'),
                ('FAQ',         WEB_URL + '/faq/'),
                ('Glossary',    WEB_URL + '/gloss/'),
                ('Quick Links', WEB_URL + '/quicklinks/'),
                ('Privacy',     WEB_URL + '/privacy/'),
                ('Legal',       WEB_URL + '/legal/'),
                )

# Plugins
PLUGIN_PATHS = ['S:\\Documents\\GitHub\\pelican-plugins', 'C:\\Users\\User\\Documents\\GitHub\\pelican-plugins']
# PLUGINS = ['assets', 'minify', 'sitemap', 'optimize_images']
PLUGINS = ['pelican_alias',
           'assets',
           'extended_sitemap',
           'neighbors']

USE_ASSETS = True
ASSETS_CSS = True
ASSETS_JS = False

SITEMAP = {
    "format": "xml",
}

EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.5,
        'pages': 0.8,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'weekly',
        'others': 'monthly',
    }
}

# `assets` sounds good, but I can't figure out how to get it to work for my CSS
# `better_figures_and_images` didn't seem to do what I wanted (see Projects)
# `gallery` looks good, but don't have a use here yet
# `liquid_tags` & `pelican_comment_system` might be useful...
# `optimize_images` works, but I don't have many images yet
#       - requires `jpegtran.exe` <http://jpegclub.org/jpegtran/> and
#           `optinpng.exe` <http://sourceforge.net/projects/optipng/>

# Tell Pelican to change the path to 'static/custom.css' in the output dir
# EXTRA_PATH_METADATA = {
#    '..\extras\burst_energy.css': {'path': 'css\burst_energy.css'}
# }

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Nav bar links are set expliciately above
# pages set to hidden don't show up in sitemap
# sitemap also uses the 'date' as last modified
```
