#!/usr/bin/env python
# coding: utf-8

import sys
import config

from app.auth import auth
from app.basehome import home
from app.schedulecourse import course

from flask import Flask, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from exts import db
from login import login_manager, sess
from cache import redis_ins

# 应用初始化
app = Flask(__name__)
app.config.from_object(config)

# redis session 初始化
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis_ins
sess.init_app(app)

manager = Manager(app)

db.init_app(app)

# 数据库模块初始化
migrate = Migrate(app, db)
# from models import UserModel
manager.add_command('db', MigrateCommand)

# 登录模块初始化
login_manager.init_app(app)

app.register_blueprint(home, url_prefix='')
app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(course)


# 错误处理页面
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(e):
    return render_template('error.html', error='出错了，请联系管理员!')


if __name__ == '__main__':
    [print(i) for i in app.url_map.iter_rules()]
    manager.run()
