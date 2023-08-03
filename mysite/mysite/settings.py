"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from configurations import Configuration, values

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
class Dev(Configuration):



    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure--@2(2b#jv8xytm1*-7g6+g4$az@mxmxiqpq&r&f!c7j7vxo!hz'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue(['localhost','127.0.0.1'])


    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites', # because of django allauth

        # my apps
        'home.apps.HomeConfig',
        'bposts.apps.BpostsConfig',
        'myprojects.apps.MyprojectsConfig',
        'todo.apps.TodoConfig',
        
        # django allauth
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.github',

        # extras
        'crispy_forms',
        "crispy_bootstrap4",

        # django restframework
        'rest_framework',
    ]

    # This is required for email validation, since I dont have a SMTP server in my machine
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    # crispy requirement
    CRISPY_TEMPLATE_PACK = 'bootstrap4' 
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

    AUTHENTICATION_BACKENDS = [
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',
        # `allauth` specific authentication methods, such as login by e-mail
        'allauth.account.auth_backends.AuthenticationBackend',
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

    ROOT_URLCONF = 'mysite.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            "DIRS": [BASE_DIR / "templates"],
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

    WSGI_APPLICATION = 'mysite.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


    # Password validation
    # https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value('UTC')

    USE_I18N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.2/howto/static-files/

    STATIC_URL = 'static/'
    STATICFILES_DIR = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    # check the sites field in the admin page
    SITE_ID = 1

    # this is the url to be redirected to after login
    LOGIN_REDIRECT_URL = '/'

class Prod(Dev):
    DOTENV = os.path.join(BASE_DIR, 'mysite/.env')

    DEBUG = False
    SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = values.ListValue(['localhost','127.0.0.1'])

    # check the sites field in the admin page
    # I'va already added another site throught the admin GUI
    SITE_ID = 2
