#!/usr/bin/env python
# coding: utf-8


from flask import render_template
from . import home


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/curriculum/')
def curriculum():
    return render_template('index.html')


@home.route('/brand/')
def brand():
    return render_template('index.html')
