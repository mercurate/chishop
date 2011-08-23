from conf.default import *
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG
LOCAL_DEVELOPMENT = False

if LOCAL_DEVELOPMENT:
    import sys
    sys.path.append(os.path.dirname(__file__))

ADMINS = (
     ('chishop', 'example@example.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(here, 'devdatabase.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

## Easy overriding, eg:
# from settings import DATABASES
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
try:
    # Keep custom_settings.py outside version control to keep things clean
    from custom_settings import *
except ImportError, e:
    pass

