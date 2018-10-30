# -*- coding: utf-8 -*-

# questions = ['name', 'quest', 'color']
# answers = ['shaun', 'the holy', 'red']

# for q, a in zip(questions, answers):
#     print('what is your {0}? It is {1}'.format(q, a))


# def huiwen(data):
#     data = str(data)

# #   for i in data:
# #      l.append(i)
#     l = [i for i in data]
#     if l[::-1] == l:
#         return True
#     else:
#         return False

# a = 123454321
# b = huiwen(a)
# print(b)

# # x = float(input("enter the value if x: "))
# x = 0.5
# n = term = num = 1
# sum = 0

# while n <= 100:
#     term *= x / n
#     sum += term
#     n += 1
#     if term < 0.00001:
#         break
# print('no iof time = {} and sum = {}'.format(n, sum))

# i = 1
# print('-' * 50)
# while i < 11:
#     n = 1
#     while n <= 10:
#         print('{:4d}'.format(i * n), end=' ')
#         n += 1
#     print()
#     i += 1
# print('-' * 50)

# # 两个矩阵相乘的计算
# n = int(input('enter the value of n:'))
# print('enter value for the matrix A')
# a = []
# for i in range(n):
#     a.append([int(x) for x in input(), split()])
# print('enter value for the matrix B')
# b = []
# for i in range(n):
#     b.append([int(x) for x in input().split()])
# c = []
# for i in range(n):
#     c.append([a[i][j] * b[j][i] for j in range(n)])
# print('afer matrix multiiplication')
# print('-' * 7 * n)
# for x in c:
#     for y in x:
#         print(str(y).rjust(5), end=' ')
#     print()
# print('-' * 7 * n)


# 迭代器
# class Counter(object):

#     def __init__(self, low, high):
#         self.current = low
#         self.high = high

#     def __iter__(self):
#         return self

#     def __next__(self):
# 返回下一个值直到当前值大于 high
#         if self.current > self.high:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1
# c = Counter(5, 10)
# for i in c:
#     print(i, end=' ')


# 生成器
# def my_generator():
#     print("Inside my generator")
#     yield 'a'
#     yield 'b'
#     yield 'c'
# for char in my_generator():
#     print(char)


# 每当执行到yield语句的时候，返回low的值并且生成器挂起，下次调用的时候从中断的地方执行
# def counter_generator(low, high):
#     while low <= high:
#         yield low
#         low += 1
# for i in counter_generator(5, 10):
#     print(i, end=' ')


# 闭包：由另外一个函数返回的函数
# def add_number(num):
#     def adder(number):
#         'adder 是一个闭包'
#         return num + number
#     return adder
# a_10 = add_number(10)
# print(a_10(21))


# # 装饰器
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before call")
#         result = func(*args, **kwargs)
#         print("After call")
#         return result
#     return wrapper


# @my_decorator
# def add(a, b):
#     return a + b
# add(1, 3)

