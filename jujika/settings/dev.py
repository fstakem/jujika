from jujika.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jujika_dev',
        'USER': 'jujika_user',
        'PASSWORD': db_password,
        'HOST': 'localhost',
        'PORT': '',
    }
}