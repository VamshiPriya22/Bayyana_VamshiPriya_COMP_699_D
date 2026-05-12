import os
from pathlib import Path

# ========================
# BASE CONFIG
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ai-work-planner-key'

DEBUG = True

ALLOWED_HOSTS = []

# ========================
# INSTALLED APPS (FIXED)
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ ONLY use AppConfig where it EXISTS
    'planner_modules.user_management.apps.UserManagementConfig',
    'planner_modules.job_management.apps.JobManagementConfig',
    'planner_modules.schedule_management.apps.ScheduleManagementConfig',

    # ✅ USE DIRECT MODULE (SAFE)
    'planner_modules.ai_planner_engine',
    'planner_modules.reminder_system',
    'planner_modules.report_management',
    'planner_modules.analytics_engine',
    'planner_modules.system_admin',
]

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # ✅ Good practice
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========================
# URL CONFIG
# ========================
ROOT_URLCONF = 'planner_config.urls'

# ========================
# WSGI (IMPORTANT)
# ========================
WSGI_APPLICATION = 'planner_config.wsgi.application'

# ========================
# TEMPLATES
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'ui_templates'],
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

# ========================
# DATABASE
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========================
# CUSTOM USER MODEL
# ========================
AUTH_USER_MODEL = 'user_management.CustomUser'

# ========================
# PASSWORD VALIDATION
# ========================
AUTH_PASSWORD_VALIDATORS = []

# ========================
# INTERNATIONALIZATION
# ========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ========================
# STATIC FILES
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static_assets']

# ========================
# MEDIA FILES
# ========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploaded_files'

# ========================
# AUTH REDIRECTS
# ========================
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

# ========================
# DEFAULT FIELD
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'