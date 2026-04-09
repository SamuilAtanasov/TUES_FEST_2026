"""
WSGI config for Guitar_Hub project.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Guitar_Hub.settings')

application = get_wsgi_application()
