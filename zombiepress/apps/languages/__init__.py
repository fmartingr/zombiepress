# Using this file to create needed things on the rest of the apps
from django.conf import settings
from zombiepress.apps.languages.models import Language


# Adding middlewares
settings.MIDDLEWARE_CLASSES = (
    'zombiepress.apps.languages.middleware.LanguageURLMiddleware',
) + settings.MIDDLEWARE_CLASSES


# Setting languages
languages = Language.objects.all()
settings.LANGUAGES = []
for language in languages:
    settings.LANGUAGES.append((language.code, language.name))
