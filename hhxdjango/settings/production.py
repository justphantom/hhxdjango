from .common import *
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '%j_6ej^=s!fo-olir+i5az_^wr=1#ci1s5u%e6a9s!m1cr_i=k'
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = True
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
STATIC_ROOT = "/static/"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DJANGO_DB_NAME'],
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASS'],
        'HOST': os.environ['DJANGO_DB_HOST'],
        'PORT': os.environ['DJANGO_DB_PORT'],
    }
}
