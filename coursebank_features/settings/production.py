def plugin_settings(settings):
    # Update the provided settings module with any app-specific settings.
    # For example:
        settings.FEATURES['ENABLE_MY_APP'] = True
        settings.MY_APP_POLICY = 'foo'
        settings.CORS_ORIGIN_ALLOW_ALL = True
        settings.CORS_ALLOW_CREDENTIALS = True
