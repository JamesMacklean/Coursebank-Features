def plugin_settings(settings):
    # Enable CORS headers
    settings.CORS_ALLOW_ALL_ORIGINS = True

    # Add 'corsheaders' middleware
    settings.MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

    # Optional: Customize CORS headers if needed
    settings.CORS_ALLOW_CREDENTIALS = True
    # settings.CORS_ALLOWED_ORIGINS = ['*']
    settings.CORS_ALLOWED_METHODS = ['GET', 'POST']
    settings.CORS_ALLOWED_HEADERS = ['*']

    # Update the provided settings module with any app-specific settings.
    # For example:
    settings.FEATURES['ENABLE_MY_APP'] = True
    settings.MY_APP_POLICY = 'foo'
