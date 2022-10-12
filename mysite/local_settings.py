import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['127.0.0.1', 'yujis-blog-djangoapp-0110.herokuapp.com']

SECRET_KEY = '8oe$7r6_adu4-o^)3#b4huf8r)66t=!sj5jvg9ea#p-m^2j!d_'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog_db',
        'USER': 'root',
        'PASSWORD': 'Gi4ETw3Y',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

DEBUG = True