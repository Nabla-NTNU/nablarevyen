"""
Production settings for nablarevyenv2
"""
from os import environ as env
import pymysql
from .base import *

pymysql.install_as_MySQLdb()

DEBUG = bool(env.get('DEBUG', False))
ALLOWED_HOSTS = ['revy.nabla.no']

ADMINS = (
<<<<<<< HEAD
    ('WebSjef', 'websjef@nabla.ntnu.no')
=======
    # TODO: add admin
>>>>>>> 0e9eb5eb9bd556e8900a7dc55cca53f13a389342
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get('MYSQL_DATABASE'),
        'USER': env.get('MYSQL_USER'),
        'PASSWORD': env.get('MYSQL_USER_PASSWORD'),
    }
}
