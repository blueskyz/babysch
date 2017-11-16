#encoding: utf-8
import os

# session 默认生效时间

SESSION_MAX_TIME = 300

# redis settings
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379  # Redis 服务器的端口，默认 6379
REDIS_AUTH = '1'
REDIS_DB = 0   #Redis 的 db

# db settings
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'babyschool'
USERNAME = 'root'

PASSWORD = '1'

DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = False

SECRET_KEY = '2480fhdffgsda.fsjadfhgq3hadsfsdfb'
