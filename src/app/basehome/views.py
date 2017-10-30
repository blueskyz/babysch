#!/usr/bin/env python
# coding: utf-8


from . import home


@home.route('/')
def index():
    return '<h1>Hello World zsz {}!</h1>'.format(__name__)


@home.route('/curriculum')
def curriculum():
    return template


@home.route('/brand')
def curriculum():
    return template
