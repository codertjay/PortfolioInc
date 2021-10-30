from .base import *

print('using local')
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

PAYSTACK_LIVE_KEY = config('PAYSTACK_DEBUG_LIVE_KEY', default='')
PAYSTACK_PUBLIC_KEY = config('PAYSTACK_DEBUG_PUBLIC_KEY', default='')

PARENT_HOST = '.localhost:8000'
DEFAULT_HOST = "www"
DEFAULT_REDIRECT_URL = "http://www.localhost:8000"


