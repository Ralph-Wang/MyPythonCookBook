#!/usr/bin/env python
# -*- coding: utf-8 -*-


def echo(value=None):
    print 'started next() called'
    try:
        while True:
            try:
                value = yield value
            except Exception as e:
                value = e
    except BaseException, e:
        print type(e)
    finally:
        print 'close() called'

gen = echo(1)

## 第一次调用, 初始化生成器
print gen.next() # 1

## 第一次调用时, yield 返回 None, 此时 value 为 None
print gen.next() # None

## 让上一次调用 yield 返回其参数, 并进行生成, 此时 value 为 send 的参数
print gen.send(2) # 2

## 让上一次调用的 yield 抛出异常
print gen.throw(TypeError, "Hello World") # Hello World

## 抛出 GeneratorExit (一般都是被吃掉), 结束生成
gen.close()

## 再次调用就会抛出 StopIteration
gen.next()
