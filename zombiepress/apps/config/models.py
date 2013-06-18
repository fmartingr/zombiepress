from django.db import models
from django.contrib import admin


class Preference(models.Model):
    key = models.CharField(max_length=40)
    value = models.CharField(max_length=256)
    pass_to_template = models.BooleanField(
        default=False,
        help_text="If checked, templates will have this value "
        "as part of the _config_ global template variable"
    )

    @staticmethod
    def get_config(**kwargs):
        if kwargs:
            preferences = Preference.objects.filter(**kwargs)
        else:
            preferences = Preference.objects.all()

        config = {}

        for item in preferences:
            config[item.key] = item.value

        return config

    @staticmethod
    def get(key):
        preference = Preference.objects.get(key=key)
        return preference.value


class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'pass_to_template', )
    list_filter = ('pass_to_template', )
    search_fields = ('key', 'value', )

admin.site.register(Preference, PreferenceAdmin)
