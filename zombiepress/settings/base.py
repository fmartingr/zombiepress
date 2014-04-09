from os import environ, path


gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Your Name', 'your_email@example.com'),
)

#TOP_PATH = path.normpath(path.join(path.dirname(__file__), '../../'))
BASE_PATH = path.normpath(path.join(path.dirname(__file__), '../'))

MANAGERS = ADMINS

DATABASES = {}

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '').split(',')

TIME_ZONE = environ.get('TIME_ZONE', 'Europe/Madrid')

LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'en')

SITE_ID = 1

LANGUAGES = []

USE_I18N = True
USE_L10N = True
USE_TZ = True
MULTILANGUAGE = environ.get('MULTILANGUAGE', False)

MEDIA_ROOT = environ.get('MEDIA_ROOT', path.join(BASE_PATH, 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = environ.get('STATIC_ROOT', path.join(BASE_PATH, 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    path.join(BASE_PATH, 'staticfiles'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'zombiepress.utils.ThemeFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = environ.get('SECRET_KEY', '1234567890')

TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.filesystem.Loader',
    # 'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    # Common
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Reversion
    'django.middleware.transaction.TransactionMiddleware',
    'reversion.middleware.RevisionMiddleware',
    # Security
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zombiepress.urls'

WSGI_APPLICATION = 'zombiepress.wsgi.application'

TEMPLATE_DIRS = ()

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    "zombiepress.apps.config.context.preferences",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'suit',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'django_jinja',
    'south',
    'reversion',
    'zombiepress.apps.config',
    'zombiepress.apps.languages',
    'zombiepress.apps.blog',
)

##
#   CONFIG
##

GRAPPELLI_ADMIN_TITLE = 'Zombiepress'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
