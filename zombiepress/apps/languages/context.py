from django.conf import settings


def languages_list(request):
    if settings.MULTILANGUAGE:
        from zombiepress.apps.languages.models import Language
        languages = Language.objects.all()
        return {'languages': languages}
