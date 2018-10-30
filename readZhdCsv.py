#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import glob
import functools


def log(fn):
	@functools.wraps(fn)
    def pa(*args, **kw):
        print('start run')
        a = fn()
        print('end')
        return a
    return pa


@log
# 获取当前路径及其目录下指定后缀的文件名
def getDirFile(fileType='csv'):
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
        data = f.readlines()  # .decode('gb2312')
    data = [list(i.split(',')) for i in data]
    return data


# 对数据进行筛选，并写入文件。文件格式为cass7.0 dat 格式
def outputCass(fileName, data, typeName=('点名', 'N', 'E', 'Z')):
    dataIndex = [data[0].index(i) for i in typeName]
    del data[0]
    # 文件后缀为3个字符的适用
    with open(fileName[:-3] + 'dat', 'w') as f:
        for i in data:
            dataList = []
            if dataList:
                dataList = []
            [dataList.append(i[j]) for j in dataIndex]
            dataList.insert(1, '')
            dataList = ','.join(dataList)
            f.write('{}\n'.format(dataList))


dirName, fileName = getDirFile()
for i in fileName:
    data = getFileData(i)
    outputCass(i, data)
