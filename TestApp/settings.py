"""
Django settings for TestApp project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import pymysql

pymysql.install_as_MySQLdb()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dx!$ska&+anps@+=%^mel1-7*5-g3*i@oo_-p3yg*qf9i4+^bg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'TestProject.MyUser'
INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestProject',
    'registration',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TestApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'TestApp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testbsbd',
        'USER': 'root',
        'PASSWORD': 'Qwerty123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Omsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SESSION_COOKIE_SECURE = True
# Параметры от модуля SecurityMiddleware
# Все пояснение по каждому параметру тут -> https://djbook.ru/rel1.9/ref/middleware.html#django.middleware.security.SecurityMiddleware

SECURE_HSTS_INCLUDE_SUBDOMAINS = True # https://djbook.ru/rel1.9/ref/middleware.html#django.middleware.security.SecurityMiddleware
SECURE_BROWSER_XSS_FILTER = True # https://djbook.ru/rel1.9/ref/settings.html#std:setting-SECURE_BROWSER_XSS_FILTER
SECURE_CONTENT_TYPE_NOSNIFF = True # Проверка типа загружаемых файлов https://djbook.ru/rel1.9/ref/settings.html#std:setting-SECURE_CONTENT_TYPE_NOSNIFF
SECURE_HSTS_SECONDS = 0 # Нужно еще изучить https://djbook.ru/rel1.9/ref/settings.html#std:setting-SECURE_HSTS_SECONDS
SECURE_SSL_REDIRECT = False # включает доступ только по HTTPS


SECURE_PROXY_SSL_HEADER = False
# CSRF_COOKIE_HTTPONLY = True # https://djbook.ru/rel1.9/ref/settings.html
SESSION_COOKIE_AGE = 86400 # Время жизни куки (секунды)