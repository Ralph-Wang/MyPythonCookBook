#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<{0}:{1}>'.format(self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print 'Found model: {0}'.format(name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print 'Found mapping: {0} => {1}'.format(k, v)
                mappings[k] = v

        for k in mappings.keys(): # 创建实例时前清除类属性
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '{0}'".format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into {0} ({1}) values ({2})'.format(self.__table__,','.join(fields), ','.join(params))
        print sql
        print args



class User(Model):
    # 继承带有 __metaclass__ 的类, 在创建实例时也会通过元类创建
    id = IntegerField('id')
    name = StringField('name')

user = User(id=1, name='Ralph')
user.save()
