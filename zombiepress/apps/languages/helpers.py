from django.conf import settings
from jingo import register
from django.core.urlresolvers import reverse
from zombiepress.apps.languages import utils
from django.utils import translation


if settings.MULTILANGUAGE:  # Only register if needed!
    @register.function(override=True)
    def url(view_name, locale=None, *args, **kwargs):
        if not locale:
            locale = translation.get_language()
        if not utils.check_if_locale_is_available(locale):
            locale = utils.get_default_locale()
        # TODO improve this
        url = "/%s%s" % (locale, reverse(view_name, args=args, kwargs=kwargs))

        return url
