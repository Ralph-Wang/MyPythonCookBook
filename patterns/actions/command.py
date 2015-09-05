#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

class CommandReceiver(object):
    def start(self):
        print "run start command"

    def stop(self):
        print "run stop command"


class Command(object):
    """ 命令基类 """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        """ 命令唯一的公开方法 """
        pass

class StartCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.stop()

class StopCommand(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.start()

class Invoker(object):
    """ 调用者 """

    def do(self, command):
        command.execute()

if __name__ == "__main__":
    receiver = CommandReceiver()
    invoker = Invoker()
    start_command = StartCommand(receiver)
    stop_command = StopCommand(receiver)

    invoker.do(start_command)
    invoker.do(stop_command)
