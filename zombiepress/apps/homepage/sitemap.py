from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class HomeSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['homepage']

    def location(self, item):
        return reverse(item)
