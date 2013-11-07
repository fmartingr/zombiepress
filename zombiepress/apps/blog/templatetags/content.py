from pytz import timezone

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_unicode
from django.conf import settings

from django_jinja import library

from zombiepress.apps.config.models import Preference


lib = library.Library()


@lib.filter
def readmore(content):
    summary, rest = content.split(Preference.get('READMORE_TAG', '<!--readmore-->'), 1)
    return summary
