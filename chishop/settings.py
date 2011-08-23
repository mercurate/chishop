from conf.default import *
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
LOCAL_DEVELOPMENT = True

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

