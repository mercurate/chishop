from conf.default import *

# This imports from the raw settings.py, not Django-enabled settings object
from settings import *

import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('chishop', 'example@example.org'),
)

MANAGERS = ADMINS

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
DATABASES['default']['NAME'] = 'chishop'
DATABASES['default']['USER'] = 'chishop'
DATABASES['default']['PASSWORD'] = 'chishop'

## These are most likely necessary to override for production
#MEDIA_ROOT = ''
#STATIC_ROOT = ''

