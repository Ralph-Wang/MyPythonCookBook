#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import random

class Singleton(object):

    """ 线程安全的单例 """

    mutex = threading.RLock()
    _instance = None

    class _Singleton(object):
        def display(self):
            print id(self)

    def __init__(self):
        if Singleton._instance is None: # 没有实例化过, 再取得锁
            time.sleep(random.randrange(1000) * 1.0 / 1000) # 尽可能的出问题
            Singleton.mutex.acquire()
            # 取得锁后再次判断是否已经实例化
            if Singleton._instance is None:
                Singleton._instance = Singleton._Singleton()
            Singleton.mutex.release()

    def __getattr__(self, attr):
        return getattr(Singleton._instance, attr)

if __name__ == "__main__":
    def test():
        s1 = Singleton()
        s1.display()
    threads = []
    for i in xrange(10000):
        threads.append(threading.Thread(target=test))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

