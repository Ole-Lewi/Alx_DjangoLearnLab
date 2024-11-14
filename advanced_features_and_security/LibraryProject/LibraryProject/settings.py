import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'your-secret-key-here'  # Replace with a secure key in production
DEBUG = False  # Set to False in production

ALLOWED_HOSTS = []  # Add allowed hostnames or IPs for production

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    # Add your app names here, for example:
    # 'your_app',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'LibraryProject.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add your templates directory here
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

# WSGI application
WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use 'django.db.backends.postgresql' for PostgreSQL
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Directory for static files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.dbg.models.BigAutoField'
#Add these settings to ensure the browser applies additional security filters
SECURE_BROWSER_XSS_FILTER = True  #enables XSS protection on browser.
X_FRAME_OPTIONS = 'DENY'  #protects against clickjacking.
SECURE_CONTENT_TYPE_NOSNIFF = True  #protects from MIME sniffing

["bookshelf.CustomUser"]

# CSRF protection enabled to prevent CSRF attacks by adding a token to each form submission
CSRF_COOKIE_SECURE = True   #This ensures that sensitive cookies (like session and CSRF tokens) are not sent over unencrypted connections.
SESSION_COOKIE_SECURE =True

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
    # other middleware
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
# Add other directives as needed

SECURE_SSL_REDIRECT = True  # redirects all HTTP request to HTTPS.
SECURE_HSTS_SECONDS = 31536000 #instructs users to use for 1 year.
SECURE_HSTS_INCLUDE_SUBDOMAINS =True
SECURE_HSTS_PRELOAD = True


["SECURE_PROXY_SSL_HEADER", "HTTP_X_FORWARDED_PROTO", "https"]