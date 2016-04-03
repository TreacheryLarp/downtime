"""
Django settings for treachery project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PRODUCTION_MODE = os.environ.get('DJANGO_PRODUCTION', '').lower() == 'true'

if PRODUCTION_MODE:
    import dj_database_url

    DEBUG = os.environ.get('DJANGO_DEBUG', '').lower() == 'true'
    SECRET_KEY = os.environ.get('DJANGO_SECRET')
    DATABASES = {'default': dj_database_url.config()}

    EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_USER')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_PASSWORD')
    EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST')
    ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS',
                                   'localhost').split(',')

else:
    DEBUG = True
    ALLOWED_HOSTS = []
    SECRET_KEY = 'testkey'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = '465'
EMAIL_USE_SSL = True

# Application definition

INSTALLED_APPS = ('django.contrib.admin',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.messages',
                  'django.contrib.staticfiles',
                  'django.contrib.sites',
                  'django_comments',
                  'simple_history',
                  'bootstrap3',
                  'players',
                  'gamemaster', )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware', )

ROOT_URLCONF = 'treachery.urls'

WSGI_APPLICATION = 'treachery.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Template system
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# Authentication
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

# Enable site contrib module setting
SITE_ID = 1

# App version
APP_VERISON = "2.4.0"
