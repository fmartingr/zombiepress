from django.shortcuts import render_to_response
from django.template import RequestContext

from zombiepress.apps.core.views import View


class HomepageView(View):
    template = 'homepage.jinja'
    section = 'homepage'

    def get(self, request):
        context = RequestContext(request, self.data)
        return render_to_response(self.template, context_instance=context)
