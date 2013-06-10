from django.conf.urls import patterns, url


urlpatterns = patterns(
    'zombiepress.apps.blog.views',
    # Post list
    url(
        r'^$',
        'list',
        name='blog_list'
    ),
    # Single entry
    url(
        r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w\-]+)/$',
        'entry',
        name='blog_item'
    ),
)
