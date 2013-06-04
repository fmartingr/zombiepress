#from zombiepress.utils import render
from django.shortcuts import render_to_response


def list(request):
    return render_to_response('blog/list.html')


def entry(request, year, month, day, slug):
    return render_to_response('blog/entry.html')
