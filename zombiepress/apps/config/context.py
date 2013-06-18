from zombiepress.apps.config.models import Preference


def preferences(request):
    preferences = Preference.objects.filter(
        pass_to_template=True
    )

    config = {}

    for item in preferences:
        config[item.key] = item.value

    return {'config': config}
