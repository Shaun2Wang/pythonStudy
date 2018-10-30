#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import glob
import functools



# @log
# 获取当前路径及其目录下指定后缀的文件名
def getDirFile(fileType='dat'):
    # 获取文件的当前路径
    dirName = os.path.abspath('')
    # 获取当前目录下后缀为.csv的文件的路径
    csv = glob.glob(dirName + '/*.' + fileType)
    # 提取文件名
    fileName = [os.path.split(f)[1] for f in csv]
    return dirName, fileName


# 获取文件内容，并将每行内容进行格式转换（tuple->list）
def getFileData(fileName):
    with open(fileName, 'r') as f:
        data = f.readlines().decode('utf-8')
    return data

def data2baogao(data):
    for i in data:
        num=len(i)//40+1
        print(num)
        for data2 in i:
            pass


# 对数据进行筛选，并写入文件。文件格式为cass7.0 dat 格式
def outputCass(fileName, data, typeName=('点名', 'N', 'E', 'Z')):
    # dataIndex = [data[0].index(i) for i in typeName]
    # del data[0]
    # 文件后缀为3个字符的适用
    with open("1" + 'dat', 'a') as f:
        f.write(data)

with open(r'C:\Users\wx030\Desktop\1.txt','rb') as f:
    data = f.readlines() #.decode('utf-8')
    for i in data:
        print(i)
num=0
for i in data:
    print(num)
    num=len(i)+num
print(num)
