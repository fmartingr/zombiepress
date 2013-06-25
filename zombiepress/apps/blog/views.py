from django.shortcuts import render_to_response
from django.template import RequestContext

from zombiepress.apps.config.models import Preference
from zombiepress.apps.blog import utils as blog_utils
from zombiepress.apps.blog.models import Entry


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
    if request.user.is_authenticated():
        item = Entry.objects.get(
            slug=slug,
            date__year=int(year),
            date__month=int(month),
            date__day=int(day)
        )
    else:
        item = Entry.objects.get(
            slug=slug,
            date__year=int(year),
            date__month=int(month),
            date__day=int(day),
            draft=False
        )

    paginator, page = blog_utils.get_paginator(request, item=item)

    data = {
        'paginator': paginator,
        'page': page,
        'section': section,
        'item': item
    }
    context = RequestContext(request, data)
    return render_to_response(
        'blog/entry.jinja2',
        context_instance=context
    )


def rss(request):
    limit = Preference.get('RSS_ITEMS', 10)
    items = Entry.objects.filter(draft=False).order_by('-date')[:limit]
    data = {
        'items': items
    }
    context = RequestContext(request, data)
    return render_to_response(
        'blog/rss.jinja2',
        context_instance=context,
        mimetype='text/xml'
    )
