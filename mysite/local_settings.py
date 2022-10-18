import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['127.0.0.1']

SECRET_KEY = '8oe$7r6_adu4-o^)3#b4huf8r)66t=!sj5jvg9ea#p-m^2j!d_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_sample',
        'USER': 'root',
        'PASSWORD': 'Gi4ETw3Y',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DEBUG = True