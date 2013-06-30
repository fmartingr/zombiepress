from django.core.paginator import Paginator
from datetime import datetime
from zombiepress.apps.blog.models import Entry
from zombiepress.apps.config.models import Preference


def get_posts(limit=None):
    items = Entry.objects.filter(
        draft=False,
        date__lt=datetime.now()
    ).order_by('-date')
        
    if limit:
        items = items[:limit]


    return items


def get_paginator(request, page_number=1, item=None):
    items = get_posts()
    entries_per_page = Preference.get('ENTRIES_PER_PAGE', 4)
    paginator = Paginator(items, entries_per_page)
    if item:
        for index, obj in enumerate(items):
            if obj == item:
                item_index = index
                break
        page_number = (item_index / entries_per_page) + 1
    page = paginator.page(page_number)

    return paginator, page
