from .common import *

DEBUG = False
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = [

] + SECRETS.get('allowed_hosts', [])

MINIFY_FRONT = True

# todo
FRONTEND_SETTINGS = {
    "client_js": {},
    "client_css": {}
}

CSRF_COOKIE_SECURE = True
