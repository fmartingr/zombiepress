import zombiepress.apps.languages.settings as languages_settings
from zombiepress.apps.languages.models import Language


def strip_language_code_from_url(path):
    locale = get_default_locale()
    locale_check = languages_settings.PATH_LOCALE_REGEX.match(path)
    if locale_check:
        custom_locale = locale_check.group('locale')
        if check_if_locale_is_available(custom_locale):
            locale = custom_locale
        path = path[3:]
    return locale, path


def check_if_locale_is_available(locale):
    return Language.objects.filter(code=locale).count()


def get_default_locale():
    return Language.objects.get(default=True).code
