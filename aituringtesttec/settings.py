import logging
import os

from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy

from environ import Env

logger = logging.getLogger("custom_logger")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger.info(f"{BASE_DIR}")

try:
    env = Env()
    env.read_env(os.path.join(BASE_DIR, ".env"))
    ENVIRONMENT = env("ENVIRONMENT")
except ImproperlyConfigured as e:
    logger.error(e)
    ENVIRONMENT = os.getenv("ENVIRONMENT")

logger.info(f"Environment:{ENVIRONMENT}")

if ENVIRONMENT == "production":
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    allowed_hosts_raw = os.getenv("ALLOWED_HOSTS")
    ALLOWED_HOSTS = allowed_hosts_raw.split(",") if allowed_hosts_raw else ["localhost"]
    PGUSER = os.getenv("PGUSER")
    PGHOST = os.getenv("PGHOST")
    PGPORT = os.getenv("PGPORT")
    PGDATABASE = os.getenv("PGDATABASE")
    PGPASSWORD = os.getenv("PGPASSWORD")
else:
    DEBUG = True
    SECRET_KEY = env("SECRET_KEY")
    ALLOWED_HOSTS = tuple(env.list("ALLOWED_HOSTS"))
    PGUSER = env("PGUSER")
    PGHOST = env("PGHOST")
    PGPORT = env("PGPORT")
    PGDATABASE = env("PGDATABASE")
    PGPASSWORD = env("PGPASSWORD")


ALLOWED_HOSTS = ["localhost", "127.0.0.1", "aituringbackend-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["http://*", "https://aituringbackend-production.up.railway.app"]


INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    # Local apps
    "cliente",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "aituringtesttec.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "aituringtesttec.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": PGDATABASE,
        "USER": PGUSER,
        "HOST": PGHOST,
        "PORT": PGPORT,
        "PASSWORD": PGPASSWORD,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "es-co"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
LOGIN_REDIRECT_URL = reverse_lazy("index")
LOGOUT_REDIRECT_URL = reverse_lazy("login")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads/")
MEDIA_URL = "/uploads/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
