#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Con la ayuda de http://moparx.com/2013/03/migrating-to-pelican-from-drupal/

AUTHOR = u'Pablo Castellano'
SITENAME = u'pablog.me'
SITESUBTITLE = u'$ cat >> /dev/blog'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'
STATIC_PATHS = ['css', 'img', 'js']
STATIC_PATHS.extend(['extra/robots.txt', 'extra/htaccess.txt', 'extra/favicon.ico'])

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'

DEFAULT_CATEGORY = 'Misc'
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
LINKS = (('BitValley', 'http://bitvalley.cc'),
         ('Marsupi', 'http://marsupi.org'),
         ('Autistici/Inventati', 'http://autistici.org'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/_pablog'),
          ('GitHub', 'https://github.com/PabloCastellano'),)

#GITHUB_URL = 'http://github.com/PabloCastellano/'
TWITTER_USERNAME = '_pablog'

DEFAULT_PAGINATION = 10

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/htaccess.txt': {'path': '.htaccess'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

MENUITEMS = (('Home', SITEURL),)

RELATIVE_URLS = True

#MD_EXTENSIONS = ['codehilite','extra']
#THEME = 'themes/moparx'

#PLUGINS = ['package.myplugin',]
# disqus, sitemap/seo


# ----------------------------------------------------------------------
# URL PATHS
# ----------------------------------------------------------------------

# Configure Pelican to output Clean URLs
AUTHOR_URL = 'author/{slug}'

ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# Atom and RSS feeds
CATEGORY_FEED_ATOM = ''
CATEGORY_FEED_RSS = '%s.rss.xml'
#FEED_ALL_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
FEED_ALL_RSS = 'rss.xml'
FEED_MAX_ITEMS = 15
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# default value is ('index', 'tags', 'categories', 'archives')
# so we just add a 'sitemap'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')

SITEMAP_SAVE_AS = 'sitemap.xml'

EXTRA_TEMPLATES_PATHS = ['templates']

# Specify theme
#THEME = "themes/myidea"
#THEME = "themes/" + "notmyidea-cms"
THEME = "themes/" + "myidea-cms"

#THEME = "themes/notmyidea"

# ----------------------------------------------------------------------
# PLUGINS
# ----------------------------------------------------------------------

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# misc
SHOW_AUTHOR = False
SHARE_TWITTER = False

#GOOGLE_ANALYTICS =
PIWIK_URL = 'stats.marsupi.org'
PIWIK_SITE_ID = '22'

DISQUS_SITENAME = 'pablogme'
