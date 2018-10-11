import os

#: Base directory containing the project. Build paths inside the project via
#: ``os.path.join(BASE_DIR, ...)``.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


#: The Django secret key is by default set from the environment. If omitted, a system check will
#: complain.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

#: SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#: By default, no hosts are allowed.
ALLOWED_HOSTS = []

#: Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'automationcommon',
    'ucamwebauth',

    'api',
]

#: Installed middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#: Root URL patterns
ROOT_URLCONF = 'gauthwebapp.urls'

#: Template loading
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

#: WSGI
WSGI_APPLICATION = 'gauthwebapp.wsgi.application'


#: Database configuration. The default settings allow configuration of the database from
#: environment variables. An environment variable named ``DJANGO_DB_<key>`` will override the
#: ``DATABASES['default'][<key>]`` setting.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


_db_envvar_prefix = 'DJANGO_DB_'
for name, value in os.environ.items():
    # Only look at variables which start with the prefix we expect
    if not name.startswith(_db_envvar_prefix):
        continue

    # Remove prefix
    name = name[len(_db_envvar_prefix):]

    # Set value
    DATABASES['default'][name] = value


#: Password validation
#:
#: .. seealso:: https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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


#: Internationalization
#:
#: .. seealso:: https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-gb'

#: Internationalization
TIME_ZONE = 'UTC'

#: Internationalization
USE_I18N = True

#: Internationalization
USE_L10N = True

#: Internationalization
USE_TZ = True

#: Static files (CSS, JavaScript, Images)
#:
#: .. seealso:: https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'

#: Authentication backends
AUTHENTICATION_BACKENDS = [
    'ucamwebauth.backends.RavenAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Raven login configuration

#: Allow the autocreation of users who have been successfully authenticated by
#: Raven but do not exist in the local database.
UCAMWEBAUTH_CREATE_USER = True

#: Redirect to this URL on log out
UCAMWEBAUTH_LOGOUT_REDIRECT = 'https://raven.cam.ac.uk/auth/logout.html'

#: Allow members who are not current members to log in?
UCAMWEBAUTH_NOT_CURRENT = False
