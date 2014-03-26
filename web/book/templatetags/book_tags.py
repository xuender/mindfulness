#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.
from django import template
register = template.Library()

@register.filter(name='ann_count')
def ann_count(chapter, user):
    '批注统计'
    return chapter.ann_count(user)
