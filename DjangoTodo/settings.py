"""
Django settings for DjangoTodo project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext, ugettext_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-@vvvdtzuuo47=#7n)5c)od!7@qa^74vlww#64hy!b40)_b_cg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_bootstrap_breadcrumbs',
    'sortable_listview',
    'bootstrap3',
    'django_bootstrap_dynamic_formsets',
    'django_filters',
    'registration',
    'rosetta',
    'DTodo',  # core application
    'DTodoRegister'  # register overrides
)

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_tools.middlewares.ThreadLocal.ThreadLocalMiddleware',
    'DjangoTodo.middleware.LastVisitedMiddleware'
)

if DEBUG:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

ROOT_URLCONF = 'DjangoTodo.urls'

TEMPLATE_DEBUG = DEBUG
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'DTodoRegister/templates'),
            os.path.join(BASE_DIR, 'DTodo/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoTodo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dtodo.db'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
LANGUAGES = (
    (LANGUAGE_CODE, 'English'),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'static/',
)

# administrators
ADMINS = (
    ('kornicameister', 'kornicameister@gmail.com')
)
MANAGERS = ADMINS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

BREADCRUMBS_TEMPLATE = 'django_bootstrap_breadcrumbs/bootstrap3.html'
_STATIC_ASSETS = STATIC_URL + 'assets/'
_BOOTSTRAP_DIR = 'bootstrap/dist/'
BOOTSTRAP3 = {
    'jquery_url': '%sjquery/dist/jquery.min.js' % _STATIC_ASSETS,
    'css_url': '%s%scss/bootstrap.min.css' % (
        _STATIC_ASSETS, _BOOTSTRAP_DIR),
    'theme_url': '%s%scss/bootstrap-theme.min.css' % (
        _STATIC_ASSETS, _BOOTSTRAP_DIR),
    'javascript_url': '%s%sjs/bootstrap.min.js' % (
        _STATIC_ASSETS, _BOOTSTRAP_DIR),
    'include_jquery': True
}

LOGIN_REDIRECT_URL = "/dtodo/"
LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"
ACCOUNT_ACTIVATION_DAYS = 7
INCLUDE_AUTH_URLS = True
INCLUDE_REGISTER_URL = True
REGISTRATION_OPEN = True  # put False to disable accounts registration
REGISTRATION_AUTO_LOGIN = True

# to be modified to send actual emails
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1023
EMAIL_HOST_USER = 'username'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'app-messages')
# to be modified to send actual emails

# debug toolbar
if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = True
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]
