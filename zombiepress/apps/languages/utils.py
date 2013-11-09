import re
from django.utils import translation
from zombiepress.apps.languages.models import Language


# TODO Move this to a conf.py file
PATH_LOCALE_REGEX = re.compile('^/(?P<locale>[\w]{2})/')


def strip_language_code_from_url(path):
    found = False
    locale = get_default_locale()
    locale_check = PATH_LOCALE_REGEX.match(path)
    if locale_check:
        custom_locale = locale_check.group('locale')
        if check_if_locale_is_available(custom_locale):
            locale = custom_locale
            found = True
        path = path[3:]
    return locale, path, found


def check_if_locale_is_available(locale):
    return Language.objects.filter(code=locale).count()


def get_active_language():
    language = Language.objects.get(code=translation.get_language())
    return language


def get_default_locale():
    return Language.objects.get(default=True).code
