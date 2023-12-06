import functools

from redis import Redis


class RedisConnection:

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = Redis(
                host='localhost',
                port=6379,
                password='qwerty',
                db=1
            )
        return cls.instance


class RedisVarsModel:

    class StringField:

        def __init__(self, key):
            self._connection = RedisConnection()
            self.key = key

        def get(self):
            try:
                return self._connection.get(self.key).decode()
            except AttributeError:
                return None


class BaseClass:

    def __init__(self):
        self.v = 1


class RedisConnect:

    def __init__(self):
        self._connection = RedisConnection()
        self.v = None  # нотация для переменных
        self.l = None  # нотация для очередей и массивов
        self.h = None  # нотация для хэш-таблиц (реализовать в дальнейшем)

    def initialize(self, vars_model=None):
        if vars_model is not None:
            self.v = vars_model()


class Vars(RedisVarsModel):

    key1 = RedisVarsModel.StringField(key='key1')


def decorator(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        print(1)
        result = func(*args, **kwargs)
        print(2)
        return result
    return _wrapper
