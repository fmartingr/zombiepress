from django.db import models
from django.contrib import admin
from django.conf import settings


###
#   
###

###
#   ENTRY
###
class Entry(models.Model):
    language = models.CharField(
        max_length=3,
        choices=settings.LANGUAGES
    )


class EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
