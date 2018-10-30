#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# def hello(fn):
# 	def wrapper():
# 		print("hello,{0}".format(fn.__name__))
# 		fn()
# 		print("goodby,{0}".format(fn.__name__))
# 	return wrapper

# @hello
# def foo():
# 	print('i am foo')

# foo()
# print(hello.__name__)


#实例1
def log(fn):
    def wrapper(*args, **kwargs):
        print('before function{0}'.format(fn.__name__))
        rst = fn(*args, **kwargs)
        print('after function{0}'.format(fn.__name__))
        return rst
    return wrapper


@log
def func():
    print('func() run.')
    return 3

if '__main__' == __name__:
    a = func()
    print(a)




# import functools

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#     print('2015-3-25')

# now()

# def logger(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @logger('DEBUG')
# def today():
#     print('2015-3-25')

# today()
# # print(today.__name__)

class Person():
    def __init__(self,first_name):
        self.first_name=first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('Expected a string')
        self._first_name=value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("can't delete this")

a = Person('andy')
print(a.first_name)
# a.first_name=42
#print(dir(a._first_name))