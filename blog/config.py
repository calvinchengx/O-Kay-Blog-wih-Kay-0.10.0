# -*- coding: utf-8 -*-
"""
The-O-Kay-Blog configuration settings

:Copyright: (c) 2009 Victor Goh <victorgoh@gmail.com>,
                     All rights reserved.
:license: BSD, see LICENSE for more details.
"""
import os

blog_name = 'Doing Good'
slogan = 'Unique Creations. Worthy Causes.'
author_name = 'Robin Low'

host = 'doinggd.appspot.com'

# Themes are located in the blog/templates/themes subfolder
theme = 'fusion-xhtml'
post_path_format = '/%(year)d/%(month)02d/%(day)02d/%(slug)s'

# Number of posts per page in the index page
posts_per_page = 5

# Default length (in words) for post summary
summary_length = 50

# The mimetype for serving HTML files.
html_mime_type = 'text/html; charset=utf-8'

# To use disqus for commenting
use_disqus = False
disqus_forum = ''

# To use PubSubHubbub
#hubbub_hub_url = 'http://pubsubhubbub.appspot.com'
hubbub_hub_url = ''

# Google Site verification file name
google_site_verification = 'my_google_site_verification.html'

# Google Analytics ID
analytics_id = 'my_analytics_id'

# A nested list of sidebar menus, for convenience. If this isn't versatile
# enough, you can edit themes/default/base.html instead.
sidebars = [
  ('Blogroll', [
  ('The O-Kay-Blog Home', 'http://www.theokayblog.com'),
  ('The Bloggart', 'http://blog.notdot.net/2009/10/Writing-a-blog-system-on-App-Engine'),
  ]),
  ('Code and Docs', [
  ('The O-Kay-Blog Project','http://code.google.com/p/theokayblog/'),
  ('Kay Framework','http://code.google.com/p/kay-framework/'),
  ('Kay Quickstart', 'http://kay-docs.shehas.net/quickstart.html'),
  ('Kay User Group', 'http://groups.google.com/group/kay-users?pli=1'),
  ]),
]

# Blog listing configuration
blogcatalog = ''

if 'SERVER_SOFTWARE' in os.environ and \
    os.environ['SERVER_SOFTWARE'].startswith('Dev'):
        devel = True
