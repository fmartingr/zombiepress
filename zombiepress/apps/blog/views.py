from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from zombiepress.apps.blog.models import Entry


section = 'blog'


def list(request):

    if request.user.is_authenticated():
        items = Entry.objects.all()
    else:
        items = Entry.objects.filter(draft=False)

    paginator = Paginator(items, 4)
    page_number = 1

    if 'page' in request.GET:
        page_number = int(request.GET['page'])

    page = paginator.page(page_number)

    data = {
        'section': section,
        'page': page,
        'page_number': page_number,
        'paginator': paginator,
    }
    context = RequestContext(request, data)
    return render_to_response('blog/list.jinja2', context_instance=context)


def entry(request, year, month, day, slug):
    return render_to_response('blog/entry.jinja2')
