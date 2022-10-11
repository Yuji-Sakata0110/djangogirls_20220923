import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '8oe$7r6_adu4-o^)3#b4huf8r)66t=!sj5jvg9ea#p-m^2j!d_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True