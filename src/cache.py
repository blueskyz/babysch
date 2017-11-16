# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Tony Wang @ 2017-11-16 01:23:24


import redis
import config


redis_ins = redis.StrictRedis(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
        db=config.REDIS_DB,
        password=config.REDIS_AUTH,
        decode_responses=False)

