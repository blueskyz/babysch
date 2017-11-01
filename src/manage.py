#!/usr/bin/env python
# coding: utf-8

import sys
import config
import exts

from app.auth import auth
from app.basehome import home
from app.schedulecourse import course

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from exts import db

app = Flask(__name__)
app.config.from_object(config)
migrate = Migrate(app, db)

from models import UserModel

manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.register_blueprint(home, url_prefix='')
app.register_blueprint(home)
app.register_blueprint(auth, url_prefix='')
app.register_blueprint(auth)
app.register_blueprint(course, url_prefix='')
app.register_blueprint(course)

manager = Manager(app)

if __name__ == '__main__':
    for i in app.url_map.iter_rules():
        print(i)
    manager.run()
