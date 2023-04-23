"""
coursebank_features Django application initialization.
"""

from django.apps import AppConfig

class CoursebankFeaturesConfig(AppConfig):
    """
    Configuration for the coursebank_features Django application.
    """

    name = 'coursebank_features'

    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'features',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'production': { 'relative_path': 'settings.production' },
                'common': { 'relative_path': 'settings.common' },
            }
        },
    }