# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Tony Wang @ 2017-11-15 00:33:07

bind='127.0.0.1:8123'
workers=3
max_requests=3000
worker_class='gevent'
loglevel='info'
access_log_format='%(h)s %(l)s %(u)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
accesslog = '/data/log/babyschool/gunicorn_access_log'
errorlog = '/data/log/babyschool/gunicorn_error_log'
