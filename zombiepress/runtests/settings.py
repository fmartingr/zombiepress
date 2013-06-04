from os import environ, path


DEBUG = bool(environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Your Name', 'your_email@example.com'),
)

#TOP_DIR = path.normpath(path.join(path.dirname(__file__), '../../'))
BASE_DIR = path.normpath(path.join(path.dirname(__file__), '../'))

MANAGERS = ADMINS

DATABASES = {}

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '').split(',')

TIME_ZONE = environ.get('TIME_ZONE', 'Europe/Madrid')

LANGUAGE_CODE = environ.get('LANGUAGE_CODE', 'en-us')

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = environ.get('MEDIA_ROOT', path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = environ.get('STATIC_ROOT', path.join(BASE_DIR, 'static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = environ.get('SECRET_KEY', '1234567890')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zombiepress.urls'

WSGI_APPLICATION = 'zombiepress.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'grappelli',
    'south',
)


##
#   TESTING ONLY
##
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'ddbb.sqlite3',
}
