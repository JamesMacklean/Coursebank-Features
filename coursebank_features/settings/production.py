def plugin_settings(settings):
    # Update the provided settings module with any app-specific settings.
    # For example:
        settings.FEATURES['ENABLE_MY_APP'] = True
        settings.MY_APP_POLICY = 'foo'
        settings.CORS_ALLOWED_ORIGINS = [
            # Add the allowed origins (domains) from which requests are allowed
            # Example: 'https://example.com'
            '*',
        ]