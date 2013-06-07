import django.core.exceptions
from django.conf import settings
from django.utils import translation
from zombiepress.apps.languages.utils import strip_language_code_from_url


class LanguageURLMiddleware(object):
    def __init__(self):
        if not settings.MULTILANGUAGE:
            raise django.core.exceptions.MiddlewareNotUsed()

    def process_request(self, request):
        locale, path = strip_language_code_from_url(request.path_info)
        translation.activate(locale)
        request.path_info = path
