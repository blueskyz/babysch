#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint


home = Blueprint('app.basehome',
                 __name__,
                 template_folder='templates',
                 url_prefix='/home')


from . import views
