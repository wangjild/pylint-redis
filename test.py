# coding: utf-8

import redis

client = redis.StrictRedis()

client.hgetall()

a = client.hgetall()

def func(c):
    return c.hgetall()  # pylint: disable=redis-bad-performance

func(client)

redis.StrictRedis().hgetall()
