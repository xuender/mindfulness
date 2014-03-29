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
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

from common.models import Message
from book.models import Star, Follow
from book.utils import toNum
from book.help import userAnns
from django.core import serializers

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

@require_http_methods(["POST", 'GET'])
def get_ann(request, uid, bid, cid):
    '获取用户对某书某章的批注'
    m = Message()
    m.ok = True
    #m.data = [{'a':1}]
    anns = userAnns(
            user = User.objects.get(id = toNum(uid)),
            cid = toNum(cid))
    data = []
    for a in anns:
        data.append(a.toDict())
    m.data = data
    return HttpResponse(m, mimetype='application/json')

def get_urls():
    return patterns('',
            url(r'^$',
                user,
                name='user'),
            url(r'^(?P<uid>\w+)$',
                info,
                name='user'),
            url(r'^(?P<uid>\w+)/(?P<bid>\w+)/(?P<cid>\w+)$',
                get_ann,
                name='get_ann'),
            )

user_urls = (get_urls(), 'user', 'user')
