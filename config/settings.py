# -*- encoding:utf-8 -*-
import os
from datetime import timedelta
from os.path import dirname, join
import environ

PROJECT_PATH = dirname(dirname(dirname(__file__)))
APPS_PATH = join(PROJECT_PATH, 'apps')
SECRET_KEY = 'f7avzcj)=)0m(85u$12-t9wq0!dw2t&)4ywbm$kg8#ibdhe38d'


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
TEST_ENV = True
env = environ.Env()
READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=False)
if READ_ENV_FILE:
    env_file = join(PROJECT_PATH, '.env')
    env.read_env(env_file)


# APP CONFIGURATION
# ------------------------------------------------------------------------------

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])


DJANGO_APPS = [
    # Default Django apps:
    "django.contrib.auth",

    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.redirects",
    "django.contrib.gis",

    # Useful template tags:
    "django.contrib.humanize",
    "django.contrib.admin",

]

LOCAL_APPS = [

]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]


# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
FIXTURE_DIRS = (
    join(PROJECT_PATH, "fixtures"),
)


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMINS = (
    ("Support", 'rmanzvila@gmail.com'),
)
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('POSTGRES_DB', default='postgres'),
        'USER': env('POSTGRES_USER', default='postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='postgres'),
        'HOST': env('POSTGRES_HOST', default='postgres'),
        'ATOMIC_REQUESTS': False
    }
}


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'es'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True


# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'web/templates'),
)

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web/templates'),],
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


# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


# PLATFORM SETTINGS
# ------------------------------------------------------------------------------
PROJECT_NAME = "Django Template - RMA"
PROJECT_AUTHOR = "Ricardo Manzanares Avila"
PROJECT_OWNER = "Loss Prevention"


TOKEN_EXPIRATION_DAYS = env.int('DJANGO_TOKEN_EXPIRATION_DAYS', default=7)
MANAGE_TRANSACTIONS = env.bool('DJANGO_MANAGE_TRANSACTIONS', default=True)


# ADMIN SETTINGS
# ------------------------------------------------------------------------------
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/')
#AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = 'account_login'

# REST FRAMEWORK CONFIGURATION
# ------------------------------------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {

    'EXCEPTION_HANDLER': 'apps.contrib.api.exceptions.formatted_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'errors',
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',
    'DEFAULT_RENDERER_CLASSES': (
        'apps.contrib.renderers.SafeJSONRenderer',
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',
    ),

    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%SZ",
}
APPEND_SLASH = False

# CACHE CONFIGURATION
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
    }
}

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000


# CACHE
CACHE_ENABLED = False