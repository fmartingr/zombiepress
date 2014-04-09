from datetime import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings

from zombiepress.apps.config.models import Preference
from zombiepress.apps.blog import utils as blog_utils
from zombiepress.apps.blog.models import Entry
from zombiepress.apps.languages.utils import get_active_language
from zombiepress.apps.core.views import View


class ListView(View):
    section = 'blog'
    template = 'blog/list.jinja'

    def get(self, request, page_number=1):
        if 'page' in request.GET:
            page_number = int(request.GET['page'])

        paginator, page = blog_utils.get_paginator(request, page_number)

        self.data['page'] = page
        self.data['page_number'] = page_number
        self.data['paginator'] = paginator

        context = RequestContext(request, self.data)
        return render_to_response(self.template, context_instance=context)


class EntryView(View):
    section = 'blog'
    template = 'blog/entry.jinja'

    def get(self, request, year, month, day, slug):
        try:
            filters = {
                'slug': slug,
                'date__year': int(year),
                'date__month': int(month),
                'date__day': int(day),
            }

            # Filter also by language if needed
            if settings.MULTILANGUAGE:
                language = get_active_language()
                filters['language'] = language

            item = Entry.objects.get(**filters)
        except Entry.DoesNotExist:
            raise Http404

        paginator, page = blog_utils.get_paginator(request, item=item)

        self.data['page'] = page
        self.data['paginator'] = paginator
        self.data['item'] = item

        context = RequestContext(request, self.data)
        return render_to_response(self.template, context_instance=context)


class SearchView(ListView):
    template = 'blog/search.jinja'

    def post(self, request):
        page_number = 1
        if 'page' in request.GET:
            page_number = int(request.GET['page'])

        search_query = request.POST['query']

        if not search_query:
            return HttpResponseRedirect(reverse('blog_list'))

        paginator, page = blog_utils.get_paginator(
            request, page_number, query=search_query
        )

        self.data['page'] = page
        self.data['page_number'] = page_number
        self.data['paginator'] = paginator
        self.data['search_query'] = search_query

        context = RequestContext(request, self.data)
        return render_to_response(self.template, context_instance=context)


class RSSView(View):
    template = 'blog/rss.jinja'

    def get(self, request):
        limit = Preference.get('RSS_ITEMS', 10)
        items = blog_utils.get_posts(limit=limit)
        self.data['items'] = items

        context = RequestContext(request, self.data)
        return render_to_response(
            'blog/rss.jinja',
            context_instance=context,
            mimetype='text/xml'
        )
