#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

class Subject(object):

    """ 被观察对象的基类 """

    def __init__(self):
        self._observers = set() # 被观察者知道所有观察它的人

    def attach(self, observer):
        """ 注册一个观察者 """
        self._observers.add(observer)

    def detach(self, observer):
        """ 注销观察者 """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        """ 自己有更新, 通知观察者 """
        for observer in self._observers:
            observer.update(self)

class Course(Subject):
    """ 课程对象, 可以被订阅(观察) """

    def __init__(self):
        super(Course, self).__init__()
        self._msg = None

    def get_msg(self):
        return self._msg

    def set_msg(self, msg):
        self._msg = msg
        self.notify() # 更新数据后通知观察者

    message = property(get_msg, set_msg)

class Observer(object):
    """ 观察者基类 """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, subject):
        pass

class StudentObserver(Observer):
    """ 学生, 需要及时得到课程更新通知. """
    def update(self, subject):
        print "Student observer: {0}".format(subject.message)

class TeacherObserver(Observer):
    """ 老师, 需要及时得到课程是更新信息. """
    def update(self,subject):
        print "Teacher observer: {0}".format(subject.message)

if __name__ == "__main__":
    s = StudentObserver()
    t = TeacherObserver()

    course = Course()

    course.attach(s)
    course.attach(t)

    course.message = "update with two observers"

    print "after detach"
    course.detach(t)
    course.message = "update with only observer"
