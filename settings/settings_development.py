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
    'default': {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        'CONFIG': {
            "hosts": ["redis://:dq0AZxdTloU41OTKmvcp44blxm4O5gSz@redis-11479.c17.us-east-1-4.ec2.cloud.redislabs.com:11479/0"],
            "symmetric_encryption_keys": [SECRET_KEY],
         
        },
        "ROUTING": "routing.application",
    },
}


DEBUG = True
