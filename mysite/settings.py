from pathlib import Path
import os
from decouple import config
import dj_database_url

# ----------------------------
# Base directory
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------
# Security
# ----------------------------
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-61_m28u-@m65s_v-bk(q8)g%x@k+v(9_8c!p8+-$lf1qu)2bzc"
)

DEBUG = config("DEBUG", default=True, cast=bool)  # True locally, False in production

ALLOWED_HOSTS = ["*"]  # Can restrict to your Render URL in production

CSRF_TRUSTED_ORIGINS = [
    "https://djangotutorial-production-a1bf.up.railway.app",
]

# ----------------------------
# Applications
# ----------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your apps
    "polls.apps.PollsConfig",
]

# ----------------------------
# Middleware
# ----------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # for static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ----------------------------
# URLs
# ----------------------------
ROOT_URLCONF = "mysite.urls"

# ----------------------------
# Templates
# ----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ----------------------------
# WSGI
# ----------------------------
WSGI_APPLICATION = "mysite.wsgi.application"

# ----------------------------
# Database (switch between SQLite locally and PostgreSQL in production)
# ----------------------------
if os.environ.get("DATABASE_URL"):
    # Use Render PostgreSQL
    DATABASES = {
        "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
    }
else:
    # Local development with SQLite
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# ----------------------------
# Password validation
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----------------------------
# Localization
# ----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ----------------------------
# Static files
# ----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise for static files in production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------------------
# Default primary key field
# ----------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"