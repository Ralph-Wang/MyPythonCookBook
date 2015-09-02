#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mock import Mock, call

class Foo(object):
    _fooValue = 123

    def callFoo(self):
        print "Foo:callFoo_"

    def doFoo(self, argValue):
        print "Foo:doFoo:input = ", argValue

class Bar(object):
    _barValue = 456

    def callBar(self):
        pass

    def doBar(self, argValue):
        pass

def list_spec():
    fooSpec = ["_fooValue", "callFoo", "doFoo"]

    mockFoo = Mock(spec=fooSpec, name="foo")
    print mockFoo
    print mockFoo._fooValue
    print mockFoo.callFoo()

def class_spec():

    mockFoo = Mock(spec=Foo)

    print mockFoo
    print mockFoo._fooValue
    print mockFoo.callFoo()

def return_value():
    mockFoo = Mock(return_value=456)
    print mockFoo
    print mockFoo()

def return_obj():
    mockFoo = Mock(return_value=Foo())

    mockObj = mockFoo()

    print mockObj

def side_effect_error():
    mockFoo = Mock(return_value=Foo(), side_effect=StandardError)

    try:
        mockFoo()
    except StandardError:
        print 'StandardError captured'

def side_effect_list():
    mockFoo = Mock(return_value=Foo(), side_effect=[1,2,3,4])


    while True:
        try:
            foo = mockFoo()
            print foo
        except StopIteration:
            print "StopIteration captured"
            break

def assert_called_with():
    mockFoo = Mock(spec=Foo)
    print mockFoo
    mockFoo.doFoo("narf")
    mockFoo.doFoo.assert_called_with("narf")

    mockFoo.doFoo()
    mockFoo.doFoo.assert_called_with()

    try:
        mockFoo.doFoo("zort")
        mockFoo.doFoo.assert_called_with("narf")
    except AssertionError as e:
        print e


def assert_called_once_with():
    mockFoo = Mock(spec=Foo)
    print mockFoo
    mockFoo.callFoo()
    mockFoo.callFoo.assert_called_once_with()

    try:
        mockFoo.callFoo()
        mockFoo.callFoo.assert_called_once_with()
    except AssertionError as e:
        print e

def assert_any_call():
    mockFoo = Mock(spec=Foo)
    print mockFoo

    mockFoo.callFoo()
    mockFoo.doFoo("narf")
    mockFoo.doFoo("zort")

    mockFoo.callFoo.assert_any_call()

    mockFoo.callFoo()
    mockFoo.doFoo("troz")

    mockFoo.doFoo.assert_any_call("zort")

    try:
        mockFoo.doFoo.assert_any_call("egad")
    except AssertionError as e:
        print e

def assert_has_calls():
    mockFoo = Mock(spec=Foo)
    print mockFoo

    mockFoo.callFoo()
    mockFoo.doFoo("narf")
    mockFoo.doFoo("zort")

    fooCalls = [call.callFoo(), call.doFoo("narf"), call.doFoo("zort")]
    mockFoo.assert_has_calls(fooCalls)

    fooCalls = [call.callFoo(), call.doFoo("zort"), call.doFoo("narf")]
    mockFoo.assert_has_calls(fooCalls, any_order=True)
    try:
        mockFoo.assert_has_calls(fooCalls)
    except AssertionError as e:
        print e

    fooCalls = [call.callFoo(), call.dooFoo("zort"), call.doFoo("narf")]
    try:
        mockFoo.assert_has_calls(fooCalls, any_order=True)
    except AssertionError as e:
        print e
    try:
        mockFoo.assert_has_calls(fooCalls)
    except AssertionError as e:
        print e


def attach_mock():
    mockFoo = Mock(spec=Foo)
    mockBar = Mock(spec=Bar)

    mockFoo.attach_mock(mockBar, "fooBar")
    print mockFoo
    print mockFoo.fooBar

def configure_mock():
    mockFoo = Mock(spec=Foo, return_value=123)
    print mockFoo()

    mockFoo.configure_mock(return_value = 456)
    print mockFoo()

    fooSpec = {
            "callFoo.return_value": "narf",
            "doFoo.return_value": "zort",
            "doFoo.side_effect": StandardError
            }
    mockFoo.configure_mock(**fooSpec)

    print mockFoo.callFoo()
    try:
        mockFoo.doFoo("narf")
    except StandardError:
        print "StandardError captured"

    fooSpec = {"doFoo.side_effect": None}
    mockFoo.configure_mock(**fooSpec)
    print mockFoo.doFoo("narf")

def mock_add_spec():
    mockFoo = Mock(spec=Foo)
    print mockFoo._fooValue
    mockFoo.mock_add_spec(Bar)
    print mockFoo._barValue

    try:
        mockFoo._fooValue
    except AttributeError as e:
        print e



def division():
    print "=" * 50

print "list spec"
list_spec()
print "class spec"
class_spec()

division()
print "return_value"
return_value()
division()
print "return_obj"
return_obj()

division()
print "side_effect_error"
side_effect_error()
division()
print "side_effect_list"
side_effect_list()

division()
print "assert_called_with"
assert_called_with()
division()
print "assert_called_once_with"
assert_called_once_with()
division()
print "assert_any_call"
assert_any_call()
division()
print "assert_has_calls"
assert_has_calls()

division()
print "attach_mock"
attach_mock()
division()
print "configure_mock"
configure_mock()
division()
print "mock_add_spec"
mock_add_spec()
