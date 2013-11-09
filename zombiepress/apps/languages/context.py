from django.conf import settings
from django.utils import translation
from zombiepress.apps.languages.utils import get_active_language


def languages_list(request):
    if settings.MULTILANGUAGE:
        from zombiepress.apps.languages.models import Language
        languages = Language.objects.all()
        return {'languages': languages}


def active_language(request):
    if settings.MULTILANGUAGE:
        return {'active_language': get_active_language()}
