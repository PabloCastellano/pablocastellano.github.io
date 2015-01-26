#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://pablog.me'
RELATIVE_URLS = True

DELETE_OUTPUT_DIRECTORY = True

MENUITEMS = (('Home', SITEURL),)

# Following items are often useful when publishing
PIWIK_URL = 'stats.marsupi.org'
PIWIK_SITE_ID = '22'

DISQUS_SITENAME = 'pablogme'
