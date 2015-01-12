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
STATIC_PATHS.extend(['extra/robots.txt', 'extra/htaccess.txt'])

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'

DEFAULT_CATEGORY = 'misc'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/_pablog'),
          ('github', 'https://github.com/PabloCastellano'),)

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

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Atom and RSS feeds
CATEGORY_FEED_ATOM = ''
CATEGORY_FEED_RSS = '%s.rss.xml'
FEED_ALL_ATOM = 'atom.xml'
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
