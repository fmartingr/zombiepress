from jingo import register
from django.core.urlresolvers import reverse
import jinja2


@register.function(override=False)
#@jinja2.contextfunction
def url_locale(view_name, *args, **kwargs):
    return reverse(view_name, args=args, kwargs=kwargs)
