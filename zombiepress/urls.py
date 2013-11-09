from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from zombiepress.utils import set_current_theme
from zombiepress.apps.blog.sitemap import BlogSitemap
from zombiepress.apps.homepage.sitemap import HomeSitemap

# Setting admin
admin.autodiscover()

# Theming
set_current_theme()

# Sitemap
sitemaps = {
    'home': HomeSitemap,
    'blog': BlogSitemap,
}

# Urls
urlpatterns = patterns(
    '',
    # Grappelli
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Projects
    #url(r'^/', include('zombiepress.projects.urls')),

    # Blog
    url(r'^blog/', include('zombiepress.apps.blog.urls')),

    # Home
    url(r'^$', include('zombiepress.apps.homepage.urls')),
    url(r'^sitemap\.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}
    )

)

# Force static files if debugging
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
