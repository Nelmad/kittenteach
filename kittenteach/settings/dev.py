from .common import *

DEBUG = True
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = [

] + SECRETS.get('allowed_hosts', [])

MINIFY_FRONT = False

# todo
FRONTEND_SETTINGS = {
    "client_js": [
        # lib
        "/core/js/lib/js.cookie.js",

        # custom
        "/core/js/csrf.js",
        "/core/js/main.js",
        "/core/js/home.js",
        "/core/js/init.js"
    ],
    "client_css": []
}

CSRF_COOKIE_SECURE = False
