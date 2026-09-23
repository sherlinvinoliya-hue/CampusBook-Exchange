from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-only-insecure-key-change-me')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
ALLOWED_HOSTS = [x.strip() for x in os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',') if x.strip()]
CSRF_TRUSTED_ORIGINS = [x.strip() for x in os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',') if x.strip()]

INSTALLED_APPS = [
    'django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions',
    'django.contrib.messages','django.contrib.staticfiles','django.contrib.sitemaps','rest_framework','accounts','books','interactions'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware'
]
ROOT_URLCONF = 'config.urls'
TEMPLATES = [{
    'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,
    'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}
}]
WSGI_APPLICATION='config.wsgi.application'
ASGI_APPLICATION='config.asgi.application'
DATABASES={'default': dj_database_url.config(default=f"sqlite:///{BASE_DIR/'db.sqlite3'}", conn_max_age=600)}
AUTH_PASSWORD_VALIDATORS=[
 {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
 {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
 {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
 {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LANGUAGE_CODE='en-us'; TIME_ZONE='Asia/Kolkata'; USE_I18N=True; USE_TZ=True
STATIC_URL='static/'; STATIC_ROOT=BASE_DIR/'staticfiles'; STATICFILES_DIRS=[BASE_DIR/'static']
MEDIA_URL='media/'; MEDIA_ROOT=BASE_DIR/'media'
STORAGES={'staticfiles': {'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage'}, 'default': {'BACKEND':'django.core.files.storage.FileSystemStorage'}}
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
LOGIN_URL='login'; LOGIN_REDIRECT_URL='dashboard'; LOGOUT_REDIRECT_URL='home'
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL='noreply@campusbookexchange.local'
FILE_UPLOAD_MAX_MEMORY_SIZE=5*1024*1024
DATA_UPLOAD_MAX_MEMORY_SIZE=30*1024*1024
SECURE_CONTENT_TYPE_NOSNIFF=True
X_FRAME_OPTIONS='DENY'
SESSION_COOKIE_HTTPONLY=True
CSRF_COOKIE_HTTPONLY=False
if not DEBUG:
    SECURE_SSL_REDIRECT=os.getenv('SECURE_SSL_REDIRECT','True').lower()=='true'
    SESSION_COOKIE_SECURE=True; CSRF_COOKIE_SECURE=True
    SECURE_HSTS_SECONDS=int(os.getenv('SECURE_HSTS_SECONDS','3600'))
    SECURE_HSTS_INCLUDE_SUBDOMAINS=True; SECURE_HSTS_PRELOAD=True
REST_FRAMEWORK={'DEFAULT_PERMISSION_CLASSES':['rest_framework.permissions.IsAuthenticatedOrReadOnly'], 'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination','PAGE_SIZE':20}
