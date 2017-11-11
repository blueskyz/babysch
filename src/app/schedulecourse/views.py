#!/usr/bin/env python
# coding: utf-8

from flask import render_template, flash, request, redirect
import flask
from . import course
from forms import ScheduleForm
from models import ScheduleRecordModel,CourseModel
from sqlalchemy import or_
from exts import db


'''
form = AuthForm()

    # 验证手机号密码
    if form.validate_on_submit():
        phone = request.form.get('phone')
        passwd = request.form.get('passwd')
        user_info = User.query.filter_by(telephone=phone).first()
        if user_info and user_info.check_password(passwd):
            login_user(user_info)
            return redirect('/')
        else:
            flash('用户名密码不匹配')

    return render_template('auth/login.html', form=form)
'''

@course.route('/schedule/',methods = ['GET','POST'])
def schedule():
    form = ScheduleForm()
    if flask.request.method == 'GET':
        return render_template('schedule_course.html',form=form)
    else:
        form = ScheduleForm(flask.request.form)
        if form.validate_on_submit():
            phone = flask.request.form.get('phone')
            datetime = flask.request.form.get('date')
            record = ScheduleRecordModel.query.filter_by(phone=phone).first()
            result = ''
            if record:
                flash('已经预约')
            else:
                record = ScheduleRecordModel(phone=phone,date=datetime)
                # flash('预约成功')
                return redirect("/")
            # return render_template('schedule_course.html',form=form)
        else:
            error = "数据格式错误"
            return render_template('schedule_course.html',form=form)

'''
预约列表
'''
@course.route('/schedule-list/',methods=['GET'])
def schedule_list():
    schedule_list = ScheduleRecordModel.query.all()
    return render_template('schedul_list.html',schedule_list = schedule_list)






