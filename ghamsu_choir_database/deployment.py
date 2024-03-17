import os
from .settings import *
from .settings import BASE_DIR
import environ

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = [env('WEBSITE_HOSTNAME')]
CSRRF_TRUSTED_ORIGINS = ['https://' + env('WEBSITE_HOSTNAME')]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'lockdown.middleware.LockdownMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

connection_string = env('AZURE_POSTGRESS_CONNECTION_STRING')
parameters = {pair.split('='): pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['db_name'],
        'USER': parameters['user'],
        'HOST': parameters['host'],
        'PASSWORD': parameters['password'],
    }
}
