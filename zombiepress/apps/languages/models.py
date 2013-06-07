from django.conf import settings
from django.db import models
from django.contrib import admin, messages


def set_default_language(modeladmin, request, queryset):
    if queryset.count() > 1:
        messages.error(request, 'Only one language can be the default one.')
    else:
        item = queryset[0]
        item.set_default()
        messages.success(
            request,
            '%s is now the default language.' % item.name
        )

set_default_language.short_description = 'Set selected language as default'


class Language(models.Model):
    code = models.CharField(max_length=2, db_index=True, unique=True)
    name = models.CharField(max_length=40)
    default = models.BooleanField(default=False, editable=False)

    def __unicode__(self):
        return self.name

    def set_default(self):
        self.__class__.objects.filter(default=True).update(default=False)
        self.default = True
        self.save()


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'default', )

    actions = [
        set_default_language,
    ]

if settings.MULTILANGUAGE:
    admin.site.register(Language, LanguageAdmin)
