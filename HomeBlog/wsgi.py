"""
WSGI config for HomeBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/

"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomeBlog.settings")

application = get_wsgi_application()
"""

import site import os import sys
site.addsitedir('/home/pi/webprojects/HomeBlog/blogvirtualenv/lib/python3.4/site-packages')
# assuming your django settings file is at 
# '/home/myusername/mysite/mysite/settings.py'
path = '/home/pi/webprojects/HomeBlog'
if path not in sys.path:
    sys.path.append(path) 
os.environ['DJANGO_SETTINGS_MODULE'] = 'HomeBlog.settings'
# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""
