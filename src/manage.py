#!/usr/bin/env python
# coding: utf-8

import sys
import config
import exts

from app.auth import auth
from app.basehome import home
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from models import UserModel
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

app.register_blueprint(home, url_prefix='')
app.register_blueprint(home)
app.register_blueprint(auth, url_prefix='')
app.register_blueprint(auth)

manager = Manager(app)

if __name__ == '__main__':
    # for i in app.url_map.iter_rules():
    manager.run()
