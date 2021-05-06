"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from config import db



BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0xyo+7q%3d4)4l#0v@j@jnypwdem4$kx6bsrd*+jlh8qyfl-c2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.bookapp',
    'apps.login',
    # redes sociales
    'social_django',
]

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.bookapp.context_processors.category_links',
                'apps.bookapp.context_processors.boo_forms',
                # redes solciales
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = db.SQLITE


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


#STATIC_ROOT = BASE_DIR/'staticfiles'

#STATIC_URL = '/static/'
#STATICFILES_DIRS = (BASE_DIR, 'static')

###########################################

STATIC_URL = '/static/'

STATICFILES_DIRS = (BASE_DIR ,'static')
STATIC_ROOT = BASE_DIR/'static'



AUTHENTICATION_BACKENDS = [

    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',

]

# social para heroku

SOCIAL_AUTH_GITHUB_KEY = 'cc0198eeee2c417913f4'
SOCIAL_AUTH_GITHUB_SECRET = '90a8864b359a99e791110dad50ce5c48ec0647f1'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '348829594968-ieh3dq1flrkfdddq0us75bvf3t2e9ruh.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'y17E5IP_NTdsEUIqQuY9BvZr'


# social para local
#
#SOCIAL_AUTH_GITHUB_KEY = 'b678885bea53cd99c53c'
#SOCIAL_AUTH_GITHUB_SECRET = '90efc14745c5a28656bf741ed779016dac548b4d'
#
#
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '348829594968-ieh3dq1flrkfdddq0us75bvf3t2e9ruh.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'y17E5IP_NTdsEUIqQuY9BvZr'




LOGIN_REDIRECT_URL = '/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'


