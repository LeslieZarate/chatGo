# coding:utf-8
from settings import *

ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aadxxagh',
        'USER': 'aadxxagh',
        'PASSWORD': 'ZxL3aArWO63HrUUcJAY01vQ1cn81GM7f',
        'HOST': 'drona.db.elephantsql.com',
        'PORT': '',
    },
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}


DEBUG = True
