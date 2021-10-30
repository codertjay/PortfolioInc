from .base import *
from decouple import config

# Todo change database
DEBUG = False

# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRESQL_DATABASE_NAME'),
        'USER': config('POSTGRESQL_DATABASE_USER'),
        'PASSWORD': config('POSTGRESQL_DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
PARENT_HOST = 'portfolioinc.studio'
DEFAULT_HOST = "www"
DEFAULT_REDIRECT_URL = "http://www.portfolioinc.studio"

PAYSTACK_LIVE_KEY = config('PAYSTACK_LIVE_KEY', default='')
PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY', default='')

# S3 BUCKETS CONFIG
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SIGNATURE_VERSION = "s3v4"

# General optimization for faster delivery
AWS_IS_GZIPPED = True

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
