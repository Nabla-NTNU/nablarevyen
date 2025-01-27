"""
Production settings for nablarevyenv2
"""
from os import environ as env
import pymysql
from .base import *

pymysql.install_as_MySQLdb()

DEBUG = bool(env.get('DEBUG', False))
ALLOWED_HOSTS = ['revy.nabla.no']

ADMINS = [('WebSjef', 'websjef@nabla.ntnu.no')]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get('MYSQL_DATABASE'),
        'USER': env.get('MYSQL_USER'),
        'PASSWORD': env.get('MYSQL_USER_PASSWORD'),
    }
}
