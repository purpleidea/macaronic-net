# Django settings for this project.
# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *
import os
import sys

# don't enable debug mode when live on appengine, otherwise do when run locally
# https://developers.google.com/appengine/docs/python/runtime#The_Environment
DEBUG = not(os.environ['SERVER_SOFTWARE'].startswith('Google App Engine/'))
#DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('James Shubin', 'macaronic-django-appengine@shubin.ca'),
)
MANAGERS = ADMINS

TIME_ZONE = 'America/Montreal'

LANGUAGE_CODE = 'en-ca'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

SECRET_KEY = ''
from secret_key import SECRET_KEY	# pull in from external file not in git

#ROOT_URLCONF = 'urls'
ROOT_URLCONF = 'web.urls'	# for now...

SETTINGS_ROOT = os.path.dirname(__file__)
sys.path.insert(0, SETTINGS_ROOT)

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(SETTINGS_ROOT, 'static/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.filesystem.Loader',
#	'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), 'templates'),
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
)

INSTALLED_APPS = (
	'django.contrib.staticfiles',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'web',	# the website
	# Uncomment the next line to enable the admin:
	#'django.contrib.admin',
	# Uncomment the next line to enable admin documentation:
	'django.contrib.admindocs',
	'djangotoolbox',

	# djangoappengine should come last, so it can override a few manage.py commands
	'djangoappengine',
)

MIDDLEWARE_CLASSES = (
	# This loads the index definitions, so it has to come first
	'autoload.middleware.AutoloadMiddleware',

	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

## Activate django-dbindexer for the default database
#DATABASES['native'] = DATABASES['default']
#DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
#AUTOLOAD_SITECONF = 'indexes'

#DATABASES = {
#	'default': {
#		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#		'NAME': os.path.join(os.path.dirname(__file__), 'web/sqlite.db').replace('\\','/'),	# Or path to database file if using sqlite3.
#		'USER': '',	# Not used with sqlite3.
#		'PASSWORD': '',	# Not used with sqlite3.
#		'HOST': '',	# Set to empty string for localhost. Not used with sqlite3.
#		'PORT': '',	# Set to empty string for default. Not used with sqlite3.
#	}
#}

