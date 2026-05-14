import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def get_env(variable_name, default=None, to_integer=False):
    value = os.getenv(variable_name)
    if value is None:
        if default or default == 0:
            return default
        else:
            raise ValueError(
                f"{variable_name} is not presented in environment variables. Check your .env file"
            )
    if to_integer:
        return int(value)
    if str(value).lower() in ("true", "false"):
        return str(value).lower() == "true"

    return value


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = get_env("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    # Custom Apps
    'api',
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

ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_env("POSTGRES_DB"),
        "USER": get_env("POSTGRES_USER"),
        "PASSWORD": get_env("POSTGRES_PASSWORD"),
        "HOST": get_env("POSTGRES_HOST"),
        "PORT": get_env("POSTGRES_PORT")
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

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "base.renderers.CustomJSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "EXCEPTION_HANDLER": "base.exceptions.custom_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_THROTTLE_CLASSES": [],
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
