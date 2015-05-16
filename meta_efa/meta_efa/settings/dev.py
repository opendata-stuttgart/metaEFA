# coding=utf-8
"""Development settings and globals."""
from .base import *


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# ######### END DEBUG CONFIGURATION


# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ######### END EMAIL CONFIGURATION


# ######### DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'meta_efa',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# ######### TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    # 'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.profiling.ProfilingDebugPanel',
]

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# boto (not use on dev):
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': '{}.show_toolbar'.format(__name__),
    }


def show_toolbar(request):
    return DEBUG
# ######### END TOOLBAR CONFIGURATION

ENVIRONMENT = 'dev'

try:
    from .local_settings import *
except ImportError:
    print('No local settings found')
