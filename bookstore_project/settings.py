"""
Django settings for bookstore_project project.
"""

import os
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-fallback-key-if-not-set-for-local-dev')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Our custom apps
    'store.apps.StoreConfig',
    'admin_panel.apps.AdminPanelConfig',
    # Third-party apps
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Enables sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookstore_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # --- ADDED CART CONTEXT PROCESSOR ---
                'store.context_processors.cart_context',
                # ------------------------------------
            ],
            'builtins': [
                 # 'store.templatetags.custom_tags',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore_project.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore_db',
        'USER': 'anjali',
        'PASSWORD': 'anjali123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata' # Use your timezone
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images served by webserver in production)
STATIC_URL = 'static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_prod') # For production collectstatic

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Session Engine
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Authentication URLs
LOGIN_URL = 'store:login'
LOGIN_REDIRECT_URL = 'store:book_list'
LOGOUT_REDIRECT_URL = 'store:book_list'

# Email Backend (Console for Development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- MEDIA FILES (User Uploaded Content) CONFIGURATION ---
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ---------------------------------------------------------