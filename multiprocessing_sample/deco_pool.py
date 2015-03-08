#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from multiprocessing import cpu_count, Pool


def timer(func):
    def _wrap(*args):
        start = time.time()
        res = func(*args)
        return res, time.time() - start
    return _wrap

class timer_class(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        start = time.time()
        res = self.func(*args)
        return res, time.time() - start

# @timer # error
def fib(n):
    cache = {0: 0, 1: 1}
    def calc(n):
        if n not in cache:
            cache[n] = calc(n-1) + calc(n-2)
        return cache[n]
    return calc(n)



# timer_fib = timer(fib) # error


# things can be pickled will work in multiprocessing.Pool

timer_fib = timer_class(fib) # work
# def timer_fib(n): # work
#     start = time.time()
#     res = fib(n)
#     return res, time.time() - start

print type(timer_fib)


pool = Pool(processes=cpu_count() * 2)

futures = []

start = time.time()
for i in xrange(100):
    future = pool.apply_async(timer_fib, args=(i,))
    futures.append(future)

elapseds = []
for future in futures:
    res, elapsed = future.get()
    elapseds.append(elapsed)

total_time = time.time() - start
print total_time
print sum(elapseds) / len(elapseds)
