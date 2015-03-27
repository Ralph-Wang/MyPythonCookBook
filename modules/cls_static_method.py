#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Fruit(object):
    total = 0

    def __init__(self, area, category, batch):
        """docstring for __init__"""
        self.area = area
        self.category = category
        self.batch = batch

    @classmethod
    def get_total(cls):
        """使用类方法来访问独立的命名空间"""
        return cls.total

    @classmethod
    def set_total(cls, value):
        """使用类方法用来创建新的命名空间"""
        cls.total = value

    @staticmethod
    def is_valid_info(fruit_info):
        """没有和类/实例相关的数据, 可以使用静态函数"""
        area, category, batch = map(int, fruit_info.split('-'))

        valid_area = area < 10
        valid_category = category < 50
        valid_batch = batch < 100

        if valid_area and valid_category and valid_batch:
            return True
        return False

    def info(self):
        """和实例相关的方法"""
        return '{area:0=2}-{category:0=2}-{batch:0=2}'.format(area=self.area,
                                                              category=self.category,
                                                              batch=self.batch)

    __repr__ = info


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass

app0 = Apple(1, 4, 9)
app1 = Apple(1, 8, 10)
app0.set_total(150)  # 更好的方式是实例记一份自己的, 类记总数

org0 = Orange(3, 6, 10)
org1 = Orange(4, 8, 18)
org0.set_total(300)

print app0
print app1
print app0.get_total()
print app1.get_total()

print org0
print org1
print org0.get_total()
print org1.get_total()

assert app0.is_valid_info('8-25-33')
