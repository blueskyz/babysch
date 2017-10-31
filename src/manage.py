#!/usr/bin/env python
# coding: utf-8

import sys

from app.auth import auth
from app.basehome import home
from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

import config
from models import UserModel
from exts import db

print('\n','分割线'.center(60,'-'),'\n')
print(db)
print('\n','分割线'.center(60,'-'),'\n')

app = Flask(__name__)
app.config.from_object(config)
db.app=app
db.init_app(app)

app.register_blueprint(home, url_prefix='')
app.register_blueprint(home)
app.register_blueprint(auth, url_prefix='')
app.register_blueprint(auth)


manager = Manager(app)
migrate = Migrate(app,db)

db.create_all()


if __name__ == '__main__':
    for i in app.url_map.iter_rules():
        print(i)
    manager.run()
