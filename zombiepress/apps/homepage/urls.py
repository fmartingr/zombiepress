from django.conf.urls import patterns, url


urlpatterns = patterns(
    'zombiepress.apps.homepage.views',
    url(
        r'^$',
        'homepage',
        name='homepage'
    ),
)
