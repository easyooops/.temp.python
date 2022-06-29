# https://redis-py.readthedocs.io/en/stable/

import redis

from conf.settings import REDIS_SETTING


# By default, each Redis instance you create will in turn create its own connection pool.
# RedisPool = redis.ConnectionPool(host = REDIS_SETTING['host'],
#                                  port=REDIS_SETTING['port'],
#                                  username=REDIS_SETTING['username'],
#                                  password=REDIS_SETTING['password'])
RedisPool = redis.ConnectionPool.from_url(REDIS_SETTING['url'])

class RedisUtil(object):
    @classmethod
    def isExist(cls, k):
        "Check is key exists. true=1 / false=0"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.exists(k)
    
    @classmethod
    def set(cls, k, v):
        "Write key/value pair. value is simple"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.set(k, v)
    
    @classmethod
    def setTTL(cls, k, v, tmSecond):
        "Write key/value with timeout second"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.setex(k, tmSecond, v)
    
    @classmethod
    def setDict(cls, k, v):
        "Write key/value pair with timeout seconds. value is complex"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.mset(k, v)
    
    @classmethod
    def setDictTTL(cls, k, v, tmSecond):
        "Write key/value pair with timeout seconds. value is complex"
        conn = redis.Redis(connection_pool=RedisPool)
        conn.mset(k, v)
        return conn.expire(k, tmSecond)

    @classmethod
    def get(cls, k):
        "Read value from key. value is simple"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.get(k)
            
    @classmethod
    def getDict(cls, k):
        "Read value from key. value is complex"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.mget(k)
    
    @classmethod
    def getTTL(cls, k):
        "Read key's timeout seconds"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.ttl(k)
    
    @classmethod
    def expire(cls, k, tmSecond):
        "Set key's timeout seconds"
        conn = redis.Redis(connection_pool=RedisPool)
        return conn.expire(k, tmSecond)