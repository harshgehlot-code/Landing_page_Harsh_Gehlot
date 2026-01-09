"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# application = get_wsgi_application()

import os
import sys

# Add project root to Python path
path = '/home/harshgehlot/Landing_page_harsh_gehlot'
if path not in sys.path:
    sys.path.append(path)

# Tell Django where settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
