# -*- coding: utf-8 -*-
"""
Development settings
- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

print("DEBUG: Loading settings from staging")

from .common import *  # noqa

# Because we're behind a reverse proxy, pay attention to where the request is coming from
USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = env('FORCE_SCRIPT_NAME', default='/diakonia/')

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['example.com']) -- In Common.py
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
# END SITE CONFIGURATION

INSTALLED_APPS += ["gunicorn", ]


# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = env('DJANGO_EMAIL_HOST', default='localhost')
EMAIL_PORT = 25
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', default='Diakonia (Testing) <noreply@dev.nds.ox.ac.uk>')
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default='[Diakonia Testing] ')
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See:
# https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader', 'django.template.loaders.app_directories.Loader', ]),
]


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
# NB: Not presently compatible with Django 1.10 on Py3 - 2016-10-03 - DjDT v1.5
#     https://github.com/jazzband/django-debug-toolbar/issues/853
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
# INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', ]
# tricks to have debug toolbar when developing with docker

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
