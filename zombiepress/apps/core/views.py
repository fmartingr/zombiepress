from django.views.generic import View as DjangoView


class View(DjangoView):
    section = None
    data = {}

    def __init__(self, *args, **kwargs):
        self.data['section'] = self.section
        return super(View, self).__init__(*args, **kwargs)
