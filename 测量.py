#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import math
cos = math.cos
sin = math.sin
tan = math.tan
rad = math.radians
deg = math.degrees


def getFileData(fileName):
    '''
    功能：获取文件的文件流
    参数：文件路径
    返回值：文件流
    '''
    with open(fileName, 'r') as f:
        data = f.readlines()  # .decode('gb2312')
        data = [list(i.replace('\n', '').split(',')) for i in data][1:]
    return data


def getXianYuan(l, data):
    '''
    功能：获取相应的曲线要素
    参数：l(里程)，data(线元要素)
    '''
    i = 0
    while i < len(data):
        if float(data[i][0]) <= l <= float(data[i][1]):
            return data[i]
        i = i + 1


def List_Str2Int(list):
    '''
    功能：将元素为字符串的列表转换为浮点类型的列表
    参数：list(元素为字符串的列表)
    '''
    listint = [float(i) for i in list]
    return listint


def dms2d(dms):
    '''
    参数：dms,例如12度34分41秒为12.3441
    返回值：以弧度为单位
    '''
    d, temp = int(dms), (dms - int(dms)) * 100
    m, s = int(temp) / 60, (temp - int(temp)) / 36
    return rad(d + m + s)


def d2dms(d):
    '''
    参数：d(弧度为单位)
    返回值：dms,例如12度34分41秒为12.3441
    '''
    d = deg(d)
    d, m, s = int(d), int(60 * d % 60), 3600 * d % 60
    dms = d + m / 100 + s / 10000
    return dms


a = math.modf(12.31)

r1 = 0.1184634425
r2 = 0.2393143352
r3 = 0.2844444444
r4 = r2
r5 = r1
v1 = 0.0469100770
v2 = 0.2307653449
v3 = 0.5
v4 = 1 - v2
v5 = 1 - v1
r = (r1, r2, r3, r4, r5)
v = (v1, v2, v3, v4, v5)


def XYA(L, list):
    '''
    功能：计算任意里程的中桩坐标及方位角
    参数：l(里程)
    起点里程：La
    终点里程：Lb
    线元长度：Ls
    起点半径：Pa
    终点半径：Pb
    起点曲率：Ka
    终点曲率：Kb
    起点方位角：Aa(弧度单位)
    任意点到线元起点的弧线长：L
    起点坐标：sX,sY
    任意点方位角：Aa(弧度单位)
    转角：LR(左为-1，右为1)
    '''
    La, Lb, sX, sY, Aa, Pa, Pb = list
    Ls = Lb - La
    L = l - La
    Aa = dms2d(Aa)

    if Pa > 0 and Pb > 0:
        LR = 1
    else:
        LR = -1

    if 0 == Pa:
        Ka = 0
    else:
        Ka = 1 / abs(Pa)

    if 0 == Pb:
        Kb = 0
    else:
        Kb = 1 / abs(Pb)

    i, sumX, sumY = 0, 0, 0
    temp1 = Ka * L
    temp2 = (Kb - Ka) * L * L / (2 * Ls)

    while i < 5:
        temp3 = Aa + LR * (v[i] * temp1 + v[i] * v[i] * temp2)
        sumX = sumX + r[i] * cos(temp3)
        sumY = sumY + r[i] * sin(temp3)
        i = i + 1
    X = L * sumX + sX
    Y = L * sumY + sY
    A = Aa + LR * (temp1 + temp2)
    return X, Y, A % (2 * math.pi)


l = 57020
data = getFileData('线元.txt')
liststr = getXianYuan(l, data)
listfloat = List_Str2Int(liststr)
x, y, a = XYA(l, listfloat)
print('X=%.4f' % x)
print('Y=%.4f' % y)
print('A=%.5f' % d2dms(a))
