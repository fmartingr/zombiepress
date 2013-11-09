from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime

from zombiepress.apps.config.models import Preference
from zombiepress.apps.blog import utils as blog_utils
from zombiepress.apps.blog.models import Entry
from zombiepress.apps.languages.utils import get_active_language


section = 'blog'


def list(request, page_number=1):
    if 'page' in request.GET:
        page_number = int(request.GET['page'])

    paginator, page = blog_utils.get_paginator(request, page_number)

    data = {
        'section': section,
        'page': page,
        'page_number': page_number,
        'paginator': paginator,
    }
    context = RequestContext(request, data)
    return render_to_response('blog/list.jinja2', context_instance=context)


def entry(request, year, month, day, slug):
    try:
        filters = {
            'slug': slug,
            'date__year': int(year),
            'date__month': int(month),
            'date__day': int(day),
        }

        if settings.MULTILANGUAGE:
            language = get_active_language()            
            filters['language'] = get_active_language()

        item = Entry.objects.get(
            **filters
        )
    except Entry.DoesNotExist:
        raise Http404

    paginator, page = blog_utils.get_paginator(request, item=item)

    data = {
        'paginator': paginator,
        'page': page,
        'section': section,
        'item': item,
    }
    context = RequestContext(request, data)
    return render_to_response(
        'blog/entry.jinja2',
        context_instance=context
    )


def rss(request):
    limit = Preference.get('RSS_ITEMS', 10)
    items = blog_utils.get_posts(limit)
    data = {
        'items': items
    }
    context = RequestContext(request, data)
    return render_to_response(
        'blog/rss.jinja2',
        context_instance=context,
        mimetype='text/xml'
    )


def search(request):
    page_number = 1
    if 'page' in request.GET:
        page_number = int(request.GET['page'])

    search_query = request.POST['query']

    if not search_query:
        return HttpResponseRedirect(reverse('blog_list'))

    paginator, page = blog_utils.get_paginator(
        request, page_number, query=search_query
    )

    data = {
        'section': section,
        'page': page,
        'page_number': page_number,
        'paginator': paginator,
        'search_query': search_query,
    }
    context = RequestContext(request, data)
    return render_to_response('blog/search.jinja2', context_instance=context)
