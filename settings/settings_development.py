# coding:utf-8
from settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chat',
        'USER': 'admin',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}



DEBUG = True
