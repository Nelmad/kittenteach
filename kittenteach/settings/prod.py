from .common import *

DEBUG = False
THUMBNAIL_DEBUG = DEBUG

ALLOWED_HOSTS = [

] + SECRETS.get('allowed_hosts', [])

MINIFY_FRONT = True

# todo
FRONTEND_SETTINGS = {
    "client_js": [],
    "client_css": []
}

# "secure" cookie - browsers may ensure that the cookie is only sent with an HTTPS connection
CSRF_COOKIE_SECURE = True

LOGGING['handlers']['telegram-error'] = {
    'level': 'ERROR',
    'class': 'kittenteach.core.utils.log.TelegramHandler',  # TODO create log.py -> TelegramHandler
    'webhook': SECRETS['telegram_webhook'],
    'formatter': 'verbose',
}

logging_handlers = LOGGING['loggers']['']['handlers']
telegram_error_handler = 'telegram-error'

if telegram_error_handler not in logging_handlers:
    logging_handlers.append(telegram_error_handler)
