# -*- coding: utf-8 -*-
import os, pytz, socket, dj_database_url, rich

DEBUG = True
ACCESS_USER = True


SITE_URL = "http://127.0.0.1:8000"


SITE_ID = 2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '#r31%45#7vgenc#%02nhdv97w#w&c9@7=vp%x$6*8))xb%_4y+'

SITE_NAME = 'Alisa'
ROOT_URLCONF = 'alisa.urls'
ALLOWED_HOSTS = ['*']
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False
SITE_ID = 3
SESSION_COOKIE_AGE = 12096000 # секунд

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
             #"class": "rich.logging.RichHandler",
            #"formatter": "rich",
             #"level": "DEBUG",
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/alisa.log',
            #'formatter': 'simple'
        },
    },
    'loggers': {
        'django.db': {
            'handlers': ['console'],
            #'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'  ),
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'  ),
        },

    },
    'django.db': {
        'level': 'DEBUG',
        'handlers': ['console','file' ],
    },
}




def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}



DATABASES = {
    'default': {
        'ENGINE':  'django.db.backends.sqlite3',
        'NAME': '/home/work/blog/alisa_api/alisa.db',


    }
}
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

INSTALLED_APPS = (
    'grappelli', #  красивый стиль админки
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blog',
    'alisa',
    'loginsys',
    'ckeditor',
    'ckeditor_uploader',
    'django_extensions',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',


)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

MIDDLEWARE_CLASSES = (

    #'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware'

)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'alisa.context_processors.alisa',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        #'OPTIONS': { 'environment' 'myproject.jinja2.environment'}
    }

]

REGEXP_MSG = "^[а-яА-ЯёЁa-zA-Z0-9@/\(\)\\\"\\\'\.\,\:\!\?\;\%\*\\\\n\\\s\-\+\$\#\ ]+$" # пробел не забыть

AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',

)

"""
CKEDITOR_CONFIGS = {
    'default': {
        'scin' : 'mono',
        'toolbar': [
            ['Source', 'Styles', 'Format'],
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Subscript', 'Superscript', 'RemoveFormat', 'Image', 'Flash', 'Table', 'HorizontalRule', 'TextColor', 'BGColor', 'Smiley', 'SpecialChar', 'Link', 'Unlink', 'Anchor', 'NumberedList', 'BulletedList', 'Outdent', 'Indent', 'Blockquote', 'CreateDiv', 'BidiLtr', 'BidiRtl', 'Language',  'Save', 'NewPage', 'Preview', 'Print', 'Templates', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', 'Undo', 'Redo', 'Find', 'Replace', 'SelectAll', 'Scayt', 'Maximize', 'ShowBlocks']],
        'height': 400,
        'width': 900,
        'removePlugins': 'stylesheetparser',
        'extraPlugins': 'codesnippet',
        'forcePasteAsPlainText': False,
    },
} """

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': [
                'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['ShowBlocks', ]},
            {'name': 'about', 'items': [
                'About', 'Preview', 'Maximize',]},

        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        #MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
             'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',


        ]),


    }
}




GOOGLE_RECAPTCHA_SECRET_KEY = '6LfkECoTAAAAAOA5Dk8IyehTxmTa08vmJKrbsNmM'
MESSAGE_LEVEL = 10
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
DEFAULT_CHARSET = 'utf8'
WSGI_APPLICATION = 'alisa.wsgi.application'
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

FACEBOOK_URLREG = "https://www.facebook.com/dialog/oauth?client_id=2028536437186913&redirect_uri=http://gorlovka.ml/auth/account_fb&response_type=code&scope=email"


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media/images/')
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'images/'

SOUTH_DATABASE_ADAPTERS = {'default': "south.db.mysql"}
CONN_MAX_AGE = 100
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'rps710@mail.ru'
EMAIL_HOST_PASSWORD = 'ghjuhfvvth900_p'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'rps710@mail.ru'

SESSION_SAVE_EVERY_REQUEST = True
POST_MORTEM = True
