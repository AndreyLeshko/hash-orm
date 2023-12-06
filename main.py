import typing

from base import RedisVarsModel as Model, decorator, RedisConnect


@decorator
class RedisVars(Model):

    def __init__(self):
        self.var1 = Model.StringField(key='some_var')


connect = RedisConnect()
connect.initialize(vars_model=RedisVars)
print(connect.v)