# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Tony Wang @ 2017-11-03 01:01:14

"""
用户登录管理
"""

import ujson
import config
from exts import cache
from flask_login import LoginManager, UserMixin
from models import UserModel

login_manager = LoginManager()

login_manager.login_view='auth.login'
login_manager.login_message='请登录'

USER_AUTH_KEY_PRE = 'auth:authened_user:{}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, UserModel):
    pass
