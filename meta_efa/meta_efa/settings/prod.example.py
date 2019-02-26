import os
from .base import *

DEBUG = False

ADMINS = (
)

ENV = 'prod'

SECRET_KEY = FIXME `pwgen 64 1`

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'meta_efa',
        'HOST': 'db',
        'USER': 'meta_efa',
        'PASSWORD': os.environ.setdefault('DB_PASS', 'NoPassInEnvFound'),
        'PORT': ''
    }
}

MEDIA_ROOT = '/opt/code/media'
STATIC_ROOT = '/opt/code/static'

USE_X_FORWARDED_HOST = True
