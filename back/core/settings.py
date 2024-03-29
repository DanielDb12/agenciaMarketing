from pathlib import Path
import os
import environ

env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') 
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS_DEV')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'danduarte241@gmail.com'
EMAIL_HOST_PASSWORD = 'dfdgzaguzvtkwnav'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACTIVE_CAMPAING_URL = "https://danduarte241.api-us1.com"
ACTIVE_CAMPAING_KEY = "507c81819d3461b6969b3b2bfe12d6792aada9cdc8b7c9f748aa74f2dc2841ee25a7ae3a"



# Application definition


DJANGO_INSTALL = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ]

PROJECT_APP = [

        'apps.blog',
        'apps.category',
        'apps.contact'


        ]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader'
    ]


INSTALLED_APPS = DJANGO_INSTALL + PROJECT_APP + THIRD_PARTY_APPS


CKEDITOR_CONFIGS={
  #'default': {
  #     'toolbar': 'Custom',
  #      'toolbar_Custom': [
  #          ['Bold', 'Italic', 'Underline'],
  #          ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
  #          ['Link', 'Unlink'],
  #          ['RemoveFormat', 'Source']
  #     ],
  #      'autoParagraph': False
  #  }

'default': {
        'toolbar': 'full',
        'autoParagraph': False
    }
	
}
CKEDITOR_UPLOAD_PATH = "media/"

        

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'../front/dist')],
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

WSGI_APPLICATION = 'core.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/assets/'


 

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'../front/dist/assets')
        ]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#lo agregamos para cuando exista un usario que quiera ingresar se registre
REST_FRAMEWORK = {
#'DEFAULT_AUTHENTICATION_CLASSES': (
 #      'rest_framework.authentication.TokenAuthentication',
  # ),
   #'DEFAULT_PERMISSION_CLASSES': (
    #    'rest_framework.permissions.IsAdminUser',
  # ),

     'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
}
#quien puede usar nuestros sitios 
CORS_ORIGIN_WHITELIST = env.list('CORS_ORIGIN_WHITELIST_DEV')
CRSF_TRUSTED_ORIGINS = env.list('CRSF_TRUSTED_ORIGINS_DEV')

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'


if not DEBUG:
    ALLOWED_HOSTS=env.list('ALLOWED_HOSTS_DEPLOY')
    CORS_ORIGIN_WHITELIST=env.list('CORS_ORIGIN_WHITELIST_DEPLOY')
    CRSF_TRUSTED_ORIGINS = env.list('CRSF_TRUSTED_ORIGINS_DEPLOY')

    DATABASES = {
            "default": env.db('DATABASE_URL'),
            }
    DATABASES["default"]["ATOMIC_REQUESTS"] = True



