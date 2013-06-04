from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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
