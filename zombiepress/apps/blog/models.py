from django.db import models
from django.contrib import admin
from django.conf import settings
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import utc
from zombiepress.apps.languages.models import Language


###
#   ENTRY
###
class Entry(models.Model):
    language = models.ForeignKey(
        Language,
        blank=True,
        null=True,
        editable=settings.MULTILANGUAGE
    )
    title = models.CharField(max_length=128)
    date = models.DateTimeField(default=datetime.now(tz=utc))
    content = models.TextField()
    slug = models.SlugField(max_length=128)
    draft = models.BooleanField(default=True)
    author = models.ForeignKey(
        User,
        editable=False,
        related_name='author'
    )

    def __unicode__(self):
        return self.title

    def status(self):
        status = 'Published'
        if self.draft:
            status = 'Draft'

        if self.date > datetime.now(tz=utc):
            status = 'Scheduled'

        return status

    class Meta:
        app_label = 'blog'
        ordering = ['-date']
        verbose_name_plural = 'Entries'


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', )
    list_display_links = ('title', )

    list_filter = ('date', )
    search_fields = ('title', 'content', )

    prepopulated_fields = {"slug": ("title",)}

    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'class': 'wysiwyg'})
        },
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super(self.__class__, self).save_model(request, obj, form, change)


admin.site.register(Entry, EntryAdmin)
