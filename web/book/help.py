#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.

"""
辅助方法，多数是数据库统计或判断
"""
from django.contrib.auth.models import Group
def getCG():
    '获取顾客组'
    return Group.objects.get(id=1)

def isCS(user):
    '判断是否是客服'
    return user.groups.filter(id=2).count() == 1
