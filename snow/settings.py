"""
Django settings for snow project.

Generated by 'django-admin startproject' using Django 2.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!8!embxlx&frd*bvlgbu^57dyyo35!&f3ovmu*==g9gr)tdwup'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
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

ROOT_URLCONF = 'snow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'snow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#MEDIA_ROOT  = os.path.join(BASE_DIR, 'media', 'assets', 'damage')
#MEDIA_URL   = '/downloads/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'contrib'),
)

STATICFILES_FINDERS = (
    # settings.STATICFILES_DIRSに設定したディレクトリからファイルを読み込む
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # アプリケーションのstaticディレクトリからファイルを読み込みむ
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
#STATIC_ROOT  = os.path.join(BASE_DIR, 'static/')
#STATIC_ROOT = str(APPS_DIR.path('static'))
#STATIC_ROOT = str(APPS_DIR.path('dist'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'contrib/'),
    #str(APPS_DIR.path('static')),
    #str(APPS_DIR.path('contrib')),
    #str(APPS_DIR.path('images'))
)

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,   # これを設定しないと怒られる
    'formatters': { # 出力フォーマットを文字列形式で指定する
        'all': {    # 出力フォーマットに`all`という名前をつける
            'format': ':'.join([
                "[%(levelname)s]",
                "%(asctime)s",
                #"%(process)d",
                #"%(thread)d",
                "%(message)s",
                #"asctime:%(asctime)s",
                #"module:%(module)s",
                #"message:%(message)s",
                #"process:%(process)d",
                #"thread:%(thread)d",
            ])
        },
    },
    'handlers': {  # ログをどこに出すかの設定
        'file': {  # どこに出すかの設定に名前をつける `file`という名前をつけている
            'level': 'DEBUG',  # DEBUG以上のログを取り扱うという意味
            'class': 'logging.FileHandler',  # ログを出力するためのクラスを指定
            'filename': os.path.join(BASE_DIR, 'logs/app.log'),  # どこに出すか
            'formatter': 'all',  # どの出力フォーマットで出すかを名前で指定
        },
        'console': { # どこに出すかの設定をもう一つ、こちらの設定には`console`という名前
            'level': 'DEBUG',
            # こちらは標準出力に出してくれるクラスを指定
            'class': 'logging.StreamHandler',
            'formatter': 'all'
        },
    },
    'loggers': {  # どんなloggerがあるかを設定する
        'default': {  # commandという名前のloggerを定義
            #'handlers': ['file', 'console'],  # 先述のfile, consoleの設定で出力
            'handlers': ['file'],  # 先述のfile, consoleの設定で出力
            'level': 'DEBUG',
        },
    },
}

# LOGIN
# ------------------------------------------------------------------------------
# Djangoでログイン画面を自作する
# https://torina.top/detail/222/
# defaults
#LOGIN_URL = '/accounts/login/'
#LOGIN_REDIRECT_URL = 'accounts/profile/'
# update
#LOGIN_URL = '/login/'      # ログイン画面のURL
LOGIN_REDIRECT_URL = '/'    # /loginに直接アクセスした場合のリダイレクト

