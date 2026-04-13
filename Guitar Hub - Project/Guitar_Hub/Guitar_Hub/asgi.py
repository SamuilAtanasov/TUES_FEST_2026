"""
ASGI config for Guitar_Hub project.

"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Guitar_Hub.settings')

application = get_asgi_application()
