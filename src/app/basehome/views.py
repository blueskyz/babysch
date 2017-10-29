#!/usr/bin/env python
# coding: utf-8


from flask import Blueprint


home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
def index():
    return '<h1>Hello World zsz {}!</h1>'.format(__name__)
