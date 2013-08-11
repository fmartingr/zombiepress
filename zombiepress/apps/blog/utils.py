from django.core.paginator import Paginator
from django.utils import translation
from django.conf import settings
from datetime import datetime
from zombiepress.apps.blog.models import Entry
from zombiepress.apps.config.models import Preference
from zombiepress.apps.languages.models import Language
from zombiepress.apps.languages.utils import get_active_language


def get_posts(limit=None):
    items = Entry.objects.filter(
        draft=False,
        date__lt=datetime.now()
    ).order_by('-date')

    if settings.MULTILANGUAGE:
        language = get_active_language()
        items = items.filter(language=language)

    if limit:
        items = items[:limit]

    return items


def get_paginator(request, page_number=1, item=None):
    item_index = None
    page = None
    items = get_posts()
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
