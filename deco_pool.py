#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import Pool, cpu_count
import time

def timer(func):
    def _wrap(*args):
        start = time.time()
        res = func(*args)
        return res, time.time() - start
    return _wrap

# @timer # error
def fib(n):
    cache = {0: 0, 1: 1}
    def calc(n):
        if n not in cache:
            cache[n] = calc(n-1) + calc(n-2)
        return cache[n]
    return calc(n)


# timer_fib = timer(fib) # error

def timer_fib(n): # work
    start = time.time()
    res = fib(n)
    return res, time.time() - start



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
