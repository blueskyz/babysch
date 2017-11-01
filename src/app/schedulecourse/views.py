#!/usr/bin/env python
# coding: utf-8


from flask import render_template
import flask
from . import course


@course.route('/schedule',methods = ['GET','POST'])
def login():
    if flask.request.method == 'GET':
        return '预约课程page'
        return render_template('login.html')
    else:
        phone = flask.request.form.get('phone')
        datetime = flask.request.form.get('time')
        return '%s成功预约%s'% phone,datetime