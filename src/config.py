#encoding: utf-8
import os

# session 默认生效时间

SESSION_MAX_TIME = 300
# redis settings
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_PASSWORD = '1'
CACHE_REDIS_DB = 0

# db settings
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'babyschool'
USERNAME = 'root'
PASSWORD = 'my-secret-pw'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = False

SECRET_KEY = os.urandom(24)
