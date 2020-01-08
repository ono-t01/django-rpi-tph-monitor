"""
Django settings for tph project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nkb$&4u$3cbhc^zsiwp2o3l+370aa56%n(*!jk3)=c-u)3&*bc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'monitor.apps.MonitorConfig',
    'compressor',
    'background_task',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tph.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'tph.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     ps.path.join(BASE_DIR, 'static'),
# ]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]


# for SASS/SCSS
# https://www.accordbox.com/blog/how-use-scss-sass-your-django-project-python-way/
# https://stackoverflow.com/questions/22515611/django-sass-compressor-django-libsass-sasscompiler-command-not-found

COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_PRECOMPILERS = (
    # ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/x-scss', 'pysassc {infile} {outfile}'),
)


PAGE_SIZE = 10

# for Django Rest Framework
# https://www.django-rest-framework.org
# https://www.django-rest-framework.org/tutorial/quickstart/

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': PAGE_SIZE,
}


# for Django Background Tasks
# https://django-background-tasks.readthedocs.io/en/latest/

# MAX_ATTEMPTS = 25
# MAX_RUN_TIME = 3600
# BACKGROUND_TASK_RUN_ASYNC = False
# BACKGROUND_TASK_ASYNC_THREADS = multiprocessing.cpu_count()
# BACKGROUND_TASK_PRIORITY_ORDERING = 'DESC'


# Logging
# https://docs.djangoproject.com/en/3.0/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': 'logs/debug.log',
        #     'formatter': 'verbose',
        # },
    },
    'loggers': {
        # 'django': {
        #     'handlers': ['file'],
        #     'level': 'WARNING',
        #     'propagate': True,
        # },
        '': {
            # 'handlers': ['console', 'file'],
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# for RPi TPH Monitor
# https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/

BME280CH1_ADDR = 0x76
BME280CH2_ADDR = 0x77

# for Development on your macOS, Ubuntu or MS-Windows

ON_RASPBERRY_PI = False


# miscs

OWNER = 'ML and AI study group.'
DATET_FORMAT = 'Y F d'
TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'r'
