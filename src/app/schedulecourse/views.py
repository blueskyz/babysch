#!/usr/bin/env python
# coding: utf-8


from flask import render_template,redirect
import flask
from . import course
from forms import ScheduleForm
from models import ScheduleRecordModel,CourseModel
from sqlalchemy import or_
from exts import db


@course.route('/schedule',methods = ['GET','POST'])
def schedule():
    print(flask.request.method)
    if flask.request.method == 'GET':
        return render_template('schedule_course.html')
    else:
        form = ScheduleForm(flask.request.form)

        if form.validate():
            phone = flask.request.form.get('phone')
            datetime = flask.request.form.get('date')
            record = ScheduleRecordModel.query.filter_by(phone=phone).first()
            result = ''
            if record:
                result = '已经预约'
            else:
                record = ScheduleRecordModel(phone=phone,date=datetime)
                db.session.add(record)
                db.session.commit()
                result = '%s成功预约%s' %(phone,datetime)
            return render_template('schedule_course.html',tag = result)
        else:
            error = "预约失败请重新预约"
            return render_template('schedule_course.html',error=error)

'''
课程列表
'''
@course.route('/schedule-list',methods=['GET'])
def schedule_list():
    schedule_list = ScheduleRecordModel.query.all()
    return render_template('schedul_list.html',schedule_list = schedule_list)

'''
预约列表
'''
@course.route('/course-list',methods=['GET'])
def course_list():
    course_list = CourseModel.query.all()
    return render_template('course_list.html',course_list = course_list)


