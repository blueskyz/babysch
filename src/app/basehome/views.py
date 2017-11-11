#!/usr/bin/env python
# coding: utf-8


from flask import render_template
from . import home
from models import CourseModel


@home.route('/')
def index():
    return render_template('home/index.html')


@home.route('/curriculum/')
def curriculum():
    course_list = CourseModel.query.all()
    return render_template('home/curriculum.html',course_list=course_list)


@home.route('/activity/')
def activity():
    return render_template('home/activity.html')


@home.route('/brand/')
def brand():
    return render_template('home/intro.html')


@home.route('/idea/')
def idea():
    return render_template('home/edition.html')


@home.route('/education/')
def education():
    return render_template('home/special.html')
