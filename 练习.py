#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random
print(random.random())
random.randint(0, 10)

# 以下为总结部分
import shutil
# 复制文件：
shutil.copyfile("oldfile", "newfile")  # oldfile和newfile都只能是文件
shutil.copy("oldfile", "newfile")  # oldfile只能是文件夹，newfile可以是文件，也可以是目标目录

# 复制文件夹：
shutil.copytree("olddir", "newdir")  # olddir和newdir都只能是目录，且newdir必须不存在

# 重命名文件（目录）
os.rename("oldname", "newname")  # 文件或目录都是使用这条命令

# 移动文件（目录）
shutil.move("oldpos", "newpos")
shutil.move("D:/知乎日报/latest/优惠券.pdf", "D:/知乎日报/past/")

# lambda表达式
stm = lambda x, y: x * y
stm(5, 2)


# 函数名称可以是一个变量
def funa():
    print("it's funa")


funb = funa
funb()


# 闭包
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

#类似于C++中的结构体
import collections
point = collections.namedtuple("point", ['x', 'y'])
p = point(1, 2)
print(p.x)
print(help(collections.namedtuple))

#piakle模块
import pickle
a = [19, '23', '天', 134]
with open(r'a.txt', 'wb') as f:
    pickle.dump(a, f)

with open(r'a.txt', 'rb') as f:
    b = pickle.load(f)
print(b)

#shelve模块
import shelve
with shelve.open(r'shv.db', writeback=True) as shv:
    shv['one'] = {'name': "wang xinxin", "age": 28}
    #写回操作需要参数：writeback=True，否则下步打印age为28
    shv['one']['age'] = 18

with shelve.open(r'shv.db', writeback=True) as shv:
    a = shv['one']
    print(a)

#多线程&锁
import threading
sum = 0
loopsum = 10000
lock = threading.Lock()


def myadd():
    global sum, loopsum
    for i in range(1, loopsum):
        lock.acquire()
        sum += 1
        lock.release()


def myMinu():
    global sum, loopsum
    for i in range(1, loopsum):
        lock.acquire()
        sum -= 1
        lock.release()


if __name__ == '__main__':
    print('strating ....{0}'.format(sum))

    t1 = threading.Thread(target=myadd, args=())
    t2 = threading.Thread(target=myMinu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Done....{0}'.format(sum))


# 获取bing每日一图，并保存在本地
import requests
import re
import time
# 以年.月.日的格式返回当前时间
local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text
reg = r"(az/hprichbg/rb/.*?.jpg)"
# 在Python的正则表达式中，有一个参数为re.S。它表示“.”（不包含外侧双引号）的作用扩展到整个字符串，包括“\n”
a = re.findall(reg, content, re.S)[0]
print(a)
picUrl = url + a
read = requests.get(picUrl)
with open(r'C:\Users\wx030\Pictures\{}.jpg'.format(local), 'wb') as f:
    f.write(read.content)