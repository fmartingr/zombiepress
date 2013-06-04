from django.conf import settings
from os import environ


def set_current_theme():
    "Get the current active theme."
    theme = environ.get('ZOMBIEPRESS_THEME', 'default')
    # TODO check if path exists!
    settings.TEMPLATE_DIRS += (
        '%s/themes/%s' % (
            settings.BASE_PATH,
            theme
        ),
    )

    settings.STATICFILES_DIRS += (
        '%s/themes/%s/static' % (
            settings.BASE_PATH,
            theme
        ),
    )
