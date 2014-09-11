# coding: utf-8

import os

SITENAME = "flask-base"

# project dir
PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# secret key
# use ``os.urandom(24)`` to generate a new one
SECRET_KEY = '\x8d\x98He\x07\x1f\x00\x8e\x90\xd2\xc5;\xe7\xebD\x1e\xebf,\x02F\x1b\xdc6'

# paths & urls
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'

# target static dir
COLLECT_STATIC_ROOT = 'static/'
COLLECT_STORAGE = 'flask.ext.collect.storage.file'

# debugging
DEBUG = True

# database
DB_URI = 'sqlite:////tmp/test.db'

# libraries
LIB = [
    'dbtools',
    'thumbs',
    'static',
    'slug',
    'user',
    'geo',
]

# web modules
WEB = [
    'layout',
]

# admin modules
ADM = [
    'backend',
]