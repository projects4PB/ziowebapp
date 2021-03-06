# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b1%tpq!64n^r^8u@ex19&7@!-j9dfg70t*gv@+t#e0zoyb$cwm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

TEMPLATE_DEBUG = True

# Application definition

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoratings',
    'rest_framework',
    'registration',
    'south',
)

INSTALLED_APPS += (
    'zioprojekt.accounts',
    'zioprojekt.events',
    'zioprojekt.offers',
    'zioprojekt.notes',
    'zioprojekt.choices',
    'zioprojekt.categories',
    'zioprojekt.webservice',
    'zioprojekt.places',
    'zioprojekt.search',
    'zioprojekt.home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zioprojekt.urls'

WSGI_APPLICATION = 'zioprojekt.wsgi.application'

# Database

import dj_database_url
DATABASES = {
	'default':dj_database_url.config(default='postgres://fvzpgzoneryvwy:q-uTVYGOav8ZwHU_nyLjfvk14R@ec2-54-247-125-187.eu-west-1.compute.amazonaws.com:5432/d2oorikqotkqpd')
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Internationalization

LANGUAGE_CODE = 'pl-pl'

LANGUAGES = (
    ('pl', u'Polski'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, '../conf/locale'),
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
    )
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

IMG_STORAGE_URL = '/storage_images/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'zioprojekt4pb@gmail.com'
EMAIL_HOST_PASSWORD = '4ZIOProjekt'
