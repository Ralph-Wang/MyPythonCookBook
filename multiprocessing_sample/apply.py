#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import Pool, cpu_count
from time import sleep
from random import random


def foo(n):
    s = random()
    sleep(s)
    return n, s


p = Pool(processes=cpu_count() * 2)

n = 100

futures = []

for i in xrange(n):
    ## apply 直接返回对应函数的结果
    # 主进程被阻塞, 直到任务完成. 没有真正利用并发优势
    # print p.apply(foo, args=(i,))

    # apply_async 返回 ApplyResult 对象, 类似 java 的 future 对象
    # 主进程可以继续进行, 后续可以用 get 获取结果
    future = p.apply_async(foo, args=(i,))
    futures.append(future)

def normal_get(futures):
    for future in futures:
        # get 返回调用结果
        # 如果调用未完成主进程会被阻塞
        print future.get()


# 关于 future 不阻塞的写法
def no_block_get(futures):
    while futures:
        done = []
        for future in futures:
            if future.ready():
                print future.get()
                done.append(future)
        for item in done:
            futures.remove(item)

## 更一种不阻塞的写法, 需要用到 deque 来做队列
def no_block_get2(futures):
    from collections import deque
    futures = deque(futures)
    while futures:
        future = futures.pop()
        if future.ready():
            print future.get()
        else:
            futures.appendleft(future)

# normal_get(futures)
# no_block_get(futures)
no_block_get2(futures)
