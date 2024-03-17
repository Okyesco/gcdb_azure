"""
WSGI config for ghamsu_choir_database project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import environ
from .settings import BASE_DIR
from django.core.wsgi import get_wsgi_application

env = environ.Env()

env.read_env(os.path.join(BASE_DIR, '.env'))


settings_module = 'ghamsu_choir_database.deployment' if 'WEBSITE_HOSTNAME' in env else 'ghamsu_choir_database.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
