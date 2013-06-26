from django.conf.urls import patterns, url


urlpatterns = patterns(
    'zombiepress.apps.blog.views',
    # Post list
    url(
        r'^$',
        'list',
        name='blog_list'
    ),
    # Post list with page
    url(
        r'^page/(?P<page_number>\d+)/$',
        'list',
        name='blog_list_page'
    ),
    # Single entry
    url(
        r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w\-]+)/$',
        'entry',
        name='blog_item'
    ),
    # RSS
    url(
        r'^rss\.xml$',
        'rss',
        name='rss'
    )
)
