from django.utils import translation
from django.utils.encoding import iri_to_uri
from django.http import HttpResponseRedirect
from zombiepress.apps.languages.utils import strip_language_code_from_url


class LanguageURLMiddleware(object):
    def process_request(self, request):
        locale, path, found = strip_language_code_from_url(request.path_info)

        # If locale is not found, we redirect to the returned locale
        # which should be the default one.
        if not found:
            return HttpResponseRedirect(iri_to_uri("/%s%s" % (locale, path)))

        # If a locale is found, we set the path without it and continue
        # as normal.
        request.path_info = path
        translation.activate(locale)
        request.LANGUAGE_CODE = translation.get_language()
