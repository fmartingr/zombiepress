from django.conf.urls import patterns, include, url
from django.contrib import admin
from zombiepress.utils import set_current_theme

# Setting admin
admin.autodiscover()

# Set current theme path
set_current_theme()


urlpatterns = patterns('',
    # Grappelli
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Homepage
    # url(r'$', include('homepage.urls'), name='homepage'),

    # Projects
    #url(r'^/', include('zombiepress.projects.urls')),

    # Blog
    url(r'^blog/', include('zombiepress.apps.blog.urls')),
)
