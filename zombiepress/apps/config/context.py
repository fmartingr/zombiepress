from zombiepress.apps.config.models import Preference


def preferences(request):
    config = Preference.get_config(pass_to_template=True)

    return {'config': config}
