# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anthony Green'
SITENAME = u'The Moxie Blog'
SITEURL = 'http://moxielogic.github.io/blog'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Retargeting GNU tools', 'http://atgreen.github.io/ggx/'),
#          ('libffi', 'http://sourceware.org/libffi/'),)
LINKS = (('Architecture', 'http://moxielogic.org/blog/pages/architecture.html'),
         ('Toolchain', 'http://moxielogic.org/blog/pages/toolchain.html'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USER_LOGO_URL = 'http://moxielogic.github.io/images/ml.png'
TAGLINE = 'A development blog for the <b>moxie processor</b>, an open source embedded soft-core processor.'
THEME = './pelican-svbhack'

DISQUS_SITENAME="moxieblog"

#GOOGLE_ANALYTICS = "UA-72427332-1"
PIWIK_ANALYTICS = "1"

STATIC_PATHS = [ 'images', 'js', 'elf' ]
