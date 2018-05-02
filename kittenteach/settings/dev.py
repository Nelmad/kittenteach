from .common import *

DEBUG = True
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = [

] + SECRETS.get('allowed_hosts', [])

MINIFY_FRONT = os.getenv('MINIFY_FRONT', 'False').lower() == 'true'

# todo
FRONTEND_SETTINGS = {
    "client_js": [
        # lib
        "/core/js/lib/js.cookie.js",

        # custom
        "/core/js/csrf.js",
        "/core/js/main.js",
        "/core/js/home.js",
        "/core/js/validators.js",
        "/core/js/auth.js",
        "/core/js/init.js"
    ],
    "client_css": []
}

CSRF_COOKIE_SECURE = False
