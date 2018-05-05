from .common import *

DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = [

] + SECRETS.get('allowed_hosts', [])

MINIFY_FRONT = os.getenv('MINIFY_FRONT', 'False').lower() == 'true'

FRONTEND_SETTINGS = get_frontend_settings(MINIFY_FRONT)

CSRF_COOKIE_SECURE = False
