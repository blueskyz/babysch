#!/usr/bin/env python
# coding: utf-8


from flask import Flask, redirect
from flask import request
from flask_script import Manager


from app.basehome import home


app = Flask(__name__)

app.register_blueprint(home, url_prefix='')
app.register_blueprint(home)


manager = Manager(app)


if __name__ == '__main__':
    for i in app.url_map.iter_rules():
        print(i)
    manager.run()
