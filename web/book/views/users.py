#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.

"""
用户页面
"""
from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

from book.models import Star, Follow
from book.utils import toNum

def user(request,):
    '查看最近100名用户'
    context = RequestContext(request)
    context['users'] = User.objects.order_by('-date_joined')[:100]
    return render_to_response('user.html', context)

def info(request, uid):
    '查看用户公开信息'
    context = RequestContext(request)
    user = User.objects.get(id = toNum(uid))
    context['user'] = user
    context['stars'] = Star.objects.filter(create_by = user)
    context['follow'] = Follow.objects.filter(create_by = user)
    return render_to_response('user_info.html', context)

def get_urls():
    return patterns('',
            url(r'^$',
                user,
                name='user'),
            url(r'^(?P<uid>\w+)$',
                info,
                name='user'),
            )

user_urls = (get_urls(), 'user', 'user')
