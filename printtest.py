#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def printall(the_list, leval):
    for x in the_list:
        if isinstance(x, list):
            print(x, leval=leval + 1)
        else:
            for tab_stop in range(leval):
                print('\t', end='\\')
        print(x)

t = [1, 6, 7, 8]
printall(t, 1)
