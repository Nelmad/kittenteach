"""
WSGI config for kittenteach project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

prod_mode = os.getenv("PRODUCTION", "").lower() == 'true'
settings = "kittenteach.settings.prod" if prod_mode else "kittenteach.settings.dev"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = get_wsgi_application()
