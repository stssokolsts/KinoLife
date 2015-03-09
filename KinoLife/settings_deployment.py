"""
Django settings for KinoLife project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '652j+^*0^vsku95oz_9o*+cd8yk9g&s2xjf5k4$-12je=iee#v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.kinolife.su']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'movie',
    'cinemate',
    'search',
    'utils',
    'disqus',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'KinoLife.urls'

WSGI_APPLICATION = 'KinoLife.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sokolenysh$KinoLife',
        'USER': 'sokolenysh',
        'PASSWORD': 'CfynfAt',
        'HOST': 'mysql.server',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)

ACCESS_TOKEN = 'f86d862402070516f8314ff4331b9091938a5af88a556c913df1272173cf00c606d6d785368c57389cc03'

APIKEY = '198c65f8632903e86b10bfe8d936c2d7aa4a0560'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

AUTHENTICATION_BACKENDS = {
    'django.contrib.auth.backends.ModelBackend'
}

SITE_ID = 1

DISQUS_API_KEY = 'Z4agMr51hvKqlpl1dLenL8Hjn0aHsmMqBxINs6Xa3pBzu5WVKD2pmWBV4L1Qx2KD'
DISQUS_WEBSITE_SHORTNAME = 'stssokolsts'


SITE_NAME = "Kinolife"
#expires_in=86400&user_id=26320727
#http://api.vk.com/blank.html#
# access_token=f86d862402070516f8314ff4331b9091938a5af88a556c913df1272173cf00c606d6d785368c57389cc03&expires_in=0&user_id=26320727

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'utils.context_processors.Kinolife',
)