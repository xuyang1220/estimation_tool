import os, sys

sys.path.append('C:/Users/yaxxu/Desktop/estimation_tool')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()