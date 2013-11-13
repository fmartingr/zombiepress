from django.db import models
from django.contrib import admin
from django.conf import settings
from django import forms
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import utc
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from zombiepress.apps.languages.utils import get_active_language
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
    tags = models.ManyToManyField('Tag', null=True)

    def __unicode__(self):
        return self.title

    def status(self):
        status = 'Published'

        if self.date > datetime.now(tz=utc):
            status = 'Scheduled'

        if self.draft:
            status = 'Draft'

        return status

    def get_absolute_url(self):
        kwargs = {
            'year': self.date.year,
            'month': self.date.strftime("%m"),
            'day': self.date.strftime("%d"),
            'slug': self.slug
        }
        if settings.MULTILANGUAGE:
            # TODO FIX THIS SHIAT
            # Doing this cuz import from helpers was failing
            language = get_active_language()
            locale = language.code
            url = "/%s%s" % (locale, reverse('blog_item', kwargs=kwargs))
        else:
            url = reverse('blog_item', kwargs=kwargs)

        return url

    class Meta:
        app_label = 'blog'
        ordering = ['-date']
        verbose_name_plural = 'Entries'


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'status', 'tag_list', 'preview_link')
    list_display_links = ('title', )

    list_filter = ('date', )
    search_fields = ('title', 'content', )

    prepopulated_fields = {"slug": ("title",)}

    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={'class': 'wysiwyg'})
        },
    }

    def preview_link(self, obj):
        return '<a href="%s">View &raquo;</a>' % (
            obj.get_absolute_url()
        )
    preview_link.allow_tags = True

    def tag_list(self, obj):
        return ", ".join([x.name for x in obj.tags.all()])

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super(self.__class__, self).save_model(request, obj, form, change)

    class Media:
        #css = {
        #    "all": ("ckeditor/redactor.css",)
        #}
        js = (
            "ckeditor/ckeditor.js",
            "js/wysiwyg.js",
        )


admin.site.register(Entry, EntryAdmin)


class Tag(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=6, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'blog'
        ordering = ['name']


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
