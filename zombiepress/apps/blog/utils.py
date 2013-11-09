from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q

from zombiepress.apps.blog.models import Entry
from zombiepress.apps.config.models import Preference


def get_posts(query=None, limit=None):
    items = Entry.objects.filter(
        draft=False,
        date__lt=datetime.now()
    )
    if query and len(query) > 0:
        items = items.filter(
            Q(title__contains=query) | Q(content__contains=query)
        )

    items = items.order_by('-date')

    if limit:
        items = items[:limit]

    return items


def get_paginator(request, page_number=1, item=None, **kwargs):
    item_index = None
    page = None
    items = get_posts(query=kwargs.get('query', None))
    entries_per_page = Preference.get('ENTRIES_PER_PAGE', 4)
    paginator = Paginator(items, entries_per_page)
    if item:
        for index, obj in enumerate(items):
            if obj == item:
                item_index = index
                break
        if item_index:
            page_number = (item_index / entries_per_page) + 1

    if page_number:
        page = paginator.page(page_number)

    return paginator, page
