#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.
from django import template
from book.models import Annotation
register = template.Library()

@register.filter(name='ann_count')
def ann_count(chapter, user):
    '批注统计'
    return chapter.ann_count(user)

@register.filter(name='user_count')
def user_count(book, chapter=None):
    '批注用户数量统计'
    if chapter:
        qs = Annotation.objects.filter(book = book, chapter = chapter)
    else:
        qs = Annotation.objects.filter(book = book)
    return qs.order_by('create_by').distinct('create_by').count()
