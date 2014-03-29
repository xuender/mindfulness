#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.

"""
纯粹工具方法
"""
SEED = 19780321
STR = 'IWLO0QVTD6ABX9PFNMU125RHK7C48SJE3ZGY'
LENGTH = 36
LEN = 3
def toNum(s):
    '''
    字符串装换成数字

    >>> toNum('9CN')
    0
    >>> toNum('0LGL')
    999999
    '''
    ns = []
    f = SEED
    for c in s.upper():
        o = STR.index(c)
        i = (o - f) % LENGTH
        ns.append(i)
        f += o
    ret = ns[0]
    for i in range(1, len(ns)):
        ret += LENGTH ** i * ns[i]
    return ret

def toStr(num):
    '''
    数值装换成字符串

    >>> toStr(0)
    '9CN'
    >>> toStr(999999)
    '0LGL'
    >>> for i in range(0, 10):
    ...  toStr(i)
    '9CN'
    'P4U'
    'F82'
    'NSR'
    'MJK'
    'UEC'
    '138'
    '2ZJ'
    '5G3'
    'RYG'
    '''
    ns = []
    if num == 0:
        ns.append(0)
    while num > 0:
        ns.append(num % LENGTH)
        num = num / LENGTH
    for i in range(len(ns), LEN):
        ns.append(0)
    ret = []
    f = SEED
    for i in ns:
        y = (i + f) % LENGTH
        ret.append(STR[y])
        f += y
    return ''.join(ret)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    for i in range(0, 20):
        print toStr(i)
