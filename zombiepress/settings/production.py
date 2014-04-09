from .base import *
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '').split(',')

TIME_ZONE = environ.get('TIME_ZONE', 'Europe/Madrid')

LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'en')

MULTILANGUAGE = environ.get('MULTILANGUAGE', False)

MEDIA_ROOT = environ.get('MEDIA_ROOT', path.join(BASE_PATH, 'media'))

STATIC_ROOT = environ.get('STATIC_ROOT', path.join(BASE_PATH, 'static'))

SECRET_KEY = environ.get('SECRET_KEY', '1234567890')

if 'SENTRY_DSN' in environ:
    SENTRY_CLIENT = 'raven.contrib.django.raven_compat.DjangoClient'
    RAVEN_CONFIG = {
        'dsn': environ.get('SENTRY_DSN'),
    }
    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )

DISQUS_SHORTNAME = 'fmartingr'
