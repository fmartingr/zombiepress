# Using this file to create needed things on the rest of the apps
from django.conf import settings
from django.db.utils import DatabaseError


if settings.MULTILANGUAGE:
    from zombiepress.apps.languages.models import Language

    # Adding middlewares
    settings.MIDDLEWARE_CLASSES = (
        'zombiepress.apps.languages.middleware.LanguageURLMiddleware',
    ) + settings.MIDDLEWARE_CLASSES

    # Adding context processors
    settings.TEMPLATE_CONTEXT_PROCESSORS += (
        'zombiepress.apps.languages.context.languages_list',
    )

    # Setting languages
    try:
        languages = Language.objects.all()
        settings.LANGUAGES = []
        for language in languages:
            settings.LANGUAGES.append((language.code, language.name))
    except DatabaseError:
        print("Languages table not found, maybe you forgot"
              " to syncdb/migrate")
