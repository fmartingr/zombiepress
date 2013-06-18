from django.shortcuts import render_to_response
from django.template import RequestContext


section = 'homepage'


def homepage(request):
    data = {
        'section': section
    }
    context = RequestContext(request, data)
    return render_to_response('homepage.jinja2', context_instance=context)
