import json
import os

from pathlib import Path

PROJECT_PACKAGE = Path(__file__).resolve().parent.parent

# The full path to the repository root.
BASE_DIR = PROJECT_PACKAGE.parent

data_dir_key = 'DATA_DIR'
DATA_DIR = Path(os.getenv(data_dir_key, BASE_DIR))

try:
    with DATA_DIR.joinpath('conf', 'secrets.json').open() as handle:
        SECRETS = json.load(handle)
except IOError:
    SECRETS = {
        'secret_key': 'secret_key',
        'superfeedr_creds': ['any@email.com', 'some_string'],
    }

SECRET_KEY = str(SECRETS['secret_key'])

ROOT_URLCONF = 'kittenteach.urls'
WSGI_APPLICATION = 'kittenteach.wsgi.application'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(BASE_DIR.joinpath('static')),
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',

    'kittenteach.core.apps.CoreConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS': 'kittenteach.api.pagination.LimitOffsetPagination'
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'kittenteach.core.context_processors.base',
                'kittenteach.core.context_processors.csrf',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'djangoproject',
    #         'USER': 'djangoproject',
    #         'HOST': SECRETS.get('db_host', ''),
    #         'PASSWORD': SECRETS.get('db_password', ''),
    #         'PORT': SECRETS.get('db_port', ''),
    #   },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = 'login'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = False
USE_L10N = False
USE_TZ = False

SESSION_COOKIE_HTTPONLY = True  # TODO ???

# TODO LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[contactor] %(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',  # DEBUG
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # This is the "catch all" logger
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

# Custom
SIXPACK_SETTINGS = {
    'host': SECRETS.get('sixpack_host', '127.0.0.1:5000'),
    'timeout': 0.5
}


def get_frontend_settings(minify):
    if minify:
        frontend_settings = {
            "client_js": [
                '/core/build/app.min.js'
            ],
            "client_css": [
                '/core/dist/core.min.css'
            ]
        }
    else:
        with open('frontend-settings.json') as handle:
            frontend_settings = json.load(handle)

        frontend_settings['client_js'].append('/core/build/app.js')

    return frontend_settings
