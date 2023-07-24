from .base import *
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost', '0.0.0.0', '127.0.0.1',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://0.0.0.0",
    "http://localhost:8080",
    "http://0.0.0.0:8080",
    "http://127.0.0.1:8080",
]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': connection_postgresql_name,
        'USER': connection_postgresql_user,
        'PASSWORD': connection_postgresql_password,
        'HOST': connection_postgresql_host,
        'PORT': connection_postgresql_port
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'