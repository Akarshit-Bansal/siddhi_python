from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-secret-key'
DEBUG = False
ALLOWED_HOSTS = [
    '.vercel.app',
    'siddhiinfonet.com',
    'www.siddhiinfonet.com',
]
CSRF_TRUSTED_ORIGINS = [
    'https://siddhiinfonet.com',
    'https://www.siddhiinfonet.com',
    'https://siddhi-python-six.vercel.app',
]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'main',
]
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dmzworlnl',
    'API_KEY': '288721815216229',
    'API_SECRET': 'p4lBA3aW5qk4rJR-GQFtI4cPp3Y',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'siddhi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'siddhi.wsgi.application'

import os
from urllib.parse import urlparse

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
       'NAME': BASE_DIR / 'db.sqlite3',
    }
}

database_url = os.environ.get('DATABASE_URL')
if database_url:
    url = urlparse(database_url)
    if url.scheme in ('postgres', 'postgresql'):
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': url.path[1:],
            'USER': url.username or '',
            'PASSWORD': url.password or '',
            'HOST': url.hostname or '',
            'PORT': url.port or '',
        }
    elif url.scheme == 'mysql':
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': url.path[1:],
            'USER': url.username or '',
            'PASSWORD': url.password or '',
            'HOST': url.hostname or '',
            'PORT': url.port or '',
        }
    elif url.scheme == 'sqlite':
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / url.path.lstrip('/'),
        } 

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'main/static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"