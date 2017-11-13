#!/usr/bin/env python
# coding: utf-8

from flask import render_template, flash, redirect
import flask
from . import course
from forms import ScheduleForm
from models import ScheduleRecordModel
from flask_login import current_user,login_required
from exts import db


@course.route('/schedule/',methods = ['GET','POST'])
def schedule():
    form = ScheduleForm()
    if flask.request.method == 'GET':
        return render_template('schedule_course.html',form=form)
    else:
        form = ScheduleForm(flask.request.form)

        age = flask.request.form.get('childage')

        print('age:',age)
        if form.validate_on_submit():
            print('\n','分割线'.center(60,'-'),'\n','数据格式正确')
            phone = form.phone.data
            age = form.childage.data
            name = form.childname.data
            record = ScheduleRecordModel.query.filter_by(phone=phone).first()
            if record:
                return redirect("/")
            else:
                model = ScheduleRecordModel(phone=phone,childage=age,childname=name)
                db.session.add(model)
                db.session.commit()
                return redirect("/")
        else:
            print('\n', '分割线'.center(60, '-'), '\n', '数据格式错误')
            return render_template('schedule_course.html',form=form)



@course.route('/schedule-list/',methods=['GET'])
@login_required
def schedule_list():
    """
    预约列表
    """
    print('页面错误')
    if not current_user.is_admin():
        print('页面错误')
        return 'No Access', 403
    else:
        schedule_list = ScheduleRecordModel.query.all()
        return render_template('schedul_list.html',schedule_list = schedule_list)


