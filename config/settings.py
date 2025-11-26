from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

import environ
import os

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'config', '.env'))


SECRET_KEY = env("SECRET_KEY")


DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["https://medisite.chbk.app/", 'medisite.chbk.app', '127.0.0.1:8000', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ["https://medisite.chbk.app/", "https://medisite.chbk.app"]


#CORS_ALLOWED_ORIGINS = [
#    "https://medisite.chbk.app/",
#]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
  "DELETE",
  "GET",
  "OPTIONS",
  "PATCH",
  "POST",
  "PUT",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd Party
    "rest_framework",
    'drf_spectacular',
    'corsheaders',
    'rest_framework_simplejwt',
    # 'django-environ',

    #Local
    "core",
    "blog",
    "accounts",
    "appointments",
    "menu",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
        'OPTIONS': {
            'auth_plugin': 'caching_sha2_password',
        }
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'medisite_db',
#         'USER': 'medisite_user',
#         'PASSWORD': '12345678',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {
#             'auth_plugin': 'caching_sha2_password',
#         }
#     }
# }


REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    "DEFAULT_AUTHENTICATION_CLASSES": (
    "rest_framework_simplejwt.authentication.JWTAuthentication",
),
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

AUTH_USER_MODEL = 'accounts.User'

