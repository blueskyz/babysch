#encoding: utf-8

import config
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache

db = SQLAlchemy()

cache = Cache(config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': config.CACHE_REDIS_HOST,
    'CACHE_REDIS_PASSWORD': config.CACHE_REDIS_PASSWORD,
    'CACHE_REDIS_DB': config.CACHE_REDIS_DB
    })
