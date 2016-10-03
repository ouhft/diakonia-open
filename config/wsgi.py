"""
WSGI config for diakonia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import environ

from django.core.wsgi import get_wsgi_application

environ.Env.read_env(env_file='config/settings/.env')

application = get_wsgi_application()
