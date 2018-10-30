#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
原始文件的后缀为point,生成kml文件。
'''
__auther__ = 'Shaun Wang'

import re
import os
import glob
# @log
# 获取当前路径及其目录下指定后缀的文件名


def getDirFile(fileType='point'):
    # 获取文件的当前路径
    dirName = os.path.abspath('')
    # 获取当前目录下后缀为.point的文件的路径
    csv = glob.glob(dirName + '/*.' + fileType)
    # 提取文件名
    fileName = [os.path.split(f)[1] for f in csv]
    return dirName, fileName


def getFileData(fileName):
    with open(fileName, 'r') as f:
        data = f.readlines()  # .decode('gb2312')
        data = [i.replace(',\n', '') for i in data]
    return data


def data2kml(data, dirName=''):
    model = ''' <Placemark>
 <name>{Name}</name>
 <description>{Description}</description>
 <Point>
 <coordinates>{Longitude},{Latitude}</coordinates>
 </Point>
 </Placemark>
'''
    data = [i.split(',') for i in data]
    models = ''
    for i in data:
        models += model.format(Name=i[0], Longitude=i[2],
                               Latitude=i[1], Description='Shuan')
    with open('point.kml', 'a') as f:
        f.write(models)


dirName, fileName = getDirFile()
for i in fileName:
    data = getFileData(i)
    data2kml(data)

# r: 只读
# w: 只写
# a: 追加
# r+: 读写
# b: 二进制
