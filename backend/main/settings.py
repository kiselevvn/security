import os
from pathlib import Path

import environ

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = os.path.dirname(BASE_DIR)

environ.Env.read_env(os.path.join(PROJECT_DIR, '.env'))

PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")
FRONTEND_DIR = os.path.join(PROJECT_DIR, "frontend")
FRONTEND_STATIC = os.path.join(FRONTEND_DIR, "static")
FRONTEND_TEMPLATES = os.path.join(FRONTEND_DIR, "templates")

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PUBLIC_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PUBLIC_DIR, "media")

STATICFILES_DIRS = [
    FRONTEND_STATIC,
]

DEBUG = env("DEBUG")


if DEBUG:
    SECRET_KEY = "django-insecure-klt#uxx_&fh#s!0c_hxern-v0et!wa(ufq!fc%r*^5%-kv=m21"
else:
    SECRET_KEY = env('SECRET_KEY')



ALLOWED_HOSTS = ["*",]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "extra_settings",
    "content",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            FRONTEND_TEMPLATES,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

DATABASES = {}

if DEBUG:
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
else:
    DATABASES["default"] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "security",
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': "db",
        'PORT': "5432",
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EXTRA_SETTINGS_VERBOSE_NAME  = "Настройки"
EXTRA_SETTINGS_DEFAULTS = [
    {
        "name": "ADDRESS",
        "type": "string",
        "value": "ул. Нансена, 85",
    },
    {
        "name": "EMAIL",
        "type": "string",
        "value": "gorizontbezopasnosti@yandex.ru",
    },
    {
        "name": "PHONE",
        "type": "string",
        "value": "+7 (950) 840-25-42",
    },
    {
        "name": "STAFF",
        "type": "string",
        "value": "250",
    },
    {
        "name": "CLIENTS",
        "type": "string",
        "value": "1500",
    },
    {
        "name": "PROJECTS",
        "type": "string",
        "value": "10000",
    },
    {
        "name": "AWARD",
        "type": "string",
        "value": "25",
    },
]
