# -*- coding: utf-8 -*- 

import re

s = '100 NORTH MAIN ROAD'

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print('ok') 

def fib(n):
    a, b = 0, 1
    while a<n:
        print(a,end=' ')
        a, b = b, a+b
    print()

fib(2000)

def fun(a, *arg, **key):
    print(a)
    for argu in arg:
        print(argu)
    keys = sorted(key.keys())
    for kw in keys:
        print(kw, ';', key[kw])

bc= 1,'m'
 
print(bc[1])

guess = input('what: ')
print(type(guess))