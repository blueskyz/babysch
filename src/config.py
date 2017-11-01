#encoding: utf-8
import os

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'babyschool'
USERNAME = 'root'
PASSWORD = '1'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = False

SECRET_KEY = os.urandom(24)
