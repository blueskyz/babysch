#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint


auth = Blueprint('app.auth',
                 __name__,
                 template_folder='templates',
                 url_prefix='/auth')


from . import views
