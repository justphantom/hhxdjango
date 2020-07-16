from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%j_6ej^=s!fo-olir+i5az_^wr=1#ci1s5u%e6a9s!m1cr_i=k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
