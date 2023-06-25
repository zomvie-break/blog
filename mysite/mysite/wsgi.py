"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')

# this import has to be done after setting the environment variable DJANGO_CONFIGURATION
from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
