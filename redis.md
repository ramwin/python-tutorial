**Xiang Wang @ 2016-12-15 17:41:21**

[github 文档](https://github.com/andymccurdy/redis-py)  

# Redis的用法
尽量参考这个文档  
[本地linux-reference下的redis参考](../linux-reference/redis.md)  
[github 上linux-reference下的redis参考](https://github.com/ramwin/linux-reference/blob/master/redis.md)  

# Basic
* Quick usage
```
import redis
```

# 单独链接

    r = redis.StrictRedis(db=0)

# 连接池

    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.StrictRedis(connection_pool=pool, decode_responses=True)

    r.get('foo')  # 如果key不存在，返回None
    r.set('foo', 'bar', ex=3600)  # 3600秒后过期。传入string也可以

    r.delete(key)   # 删除key，存在就是返回1, 否则返回0

    r.hset('dict', 'key', 'value')
    r.hdel('dict', 'key')  # 存在就返回1, 否则返回0

# 链接

# 普通链接
    r = redis.StrictRedis(host="localhost", port=6379, db=0, password=None)  # 如果服务器中断了或者无法链接 redis.exceptions.ConnectionError 连接池一样会报错。二者redis可以连接时会恢复

* `decode_responses`: 对数据进行解析，这样就不再是utf8的二进制了

# list

```
r.rpush(key, *args)  # 把args里面的数据按照顺序放入key
r.lpop(key)  # 把key里面的数据pop出来，如果没有就是None
r.lpop(['key1', 'key2'], 5)  # 随便那个key有结果就返回
r.blrange(key, 0, -1)  # must have the start and end index
```

# set
```
r.sadd(key, 'value')
r.smembers(key)  # 如果是空的，返回 set()
r.sadd(key, *set or list)  # 批量添加set

>>> r.set('key', 'bar', nx=True)
True
>>> r.set('key', 'bar', nx=True)
None
```

# ttl
```
r.ttl(key)
returns -2 if the key does not exist.
returns -1 if the key exists but has no associated expire
```

# Lock
```
try:
    with client.lock(key, blocking_timeout=5) as lock:  # 最多等你5秒
        do something expensive  # 保证同时只有一个线程跑这个
except redis.exceptions.LockError:
    # the lock wasn't acquired
```
