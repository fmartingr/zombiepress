from django.conf import settings


def config(request):
    config = {}

    # Disqus
    if hasattr(settings, 'DISQUS_SHORTNAME'):
        config['disqus_shortname'] = settings.DISQUS_SHORTNAME

    return {'config': config}
