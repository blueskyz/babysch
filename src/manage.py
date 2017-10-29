#!/usr/bin/env python
# coding: utf-8

from flask import Flask, redirect
from flask import request
from flask_script import Manager


from app.basehome import home


app = Flask(__name__)

app.register_blueprint(home)


manager = Manager(app)


@app.route('/')
def jump_home(page_name=''):
    return redirect('/kkk/',  code=301)


if __name__ == '__main__':
    manager.run()
