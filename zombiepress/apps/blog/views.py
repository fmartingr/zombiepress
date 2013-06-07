#from zombiepress.utils import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import translation


def list(request):
    context = RequestContext(request)
    return render_to_response('blog/list.jinja2', context_instance=context)


def entry(request, year, month, day, slug):
    return render_to_response('blog/entry.jinja2')
