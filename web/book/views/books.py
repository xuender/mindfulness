# -*- coding: utf-8 -*-
import json

from django.conf.urls import patterns, url, include
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

from common.models import Message
from book.models import Book, Chapter, Star, Annotation

def annotation(request):
    '显示标注弹出窗口'
    context = RequestContext(request)
    if hasattr(request, 'user') and request.user.is_authenticated():
        return render_to_response('annotation.html', context)
    return render_to_response('registration/login_modal.html', context)

def readValue(data, key, message, msg):
    '读取参数'
    if key not in data:
        message.ok = False
        message.msg = msg
    return data[key]

# 集成到book网址下的函数

@login_required
@require_http_methods(["POST"])
def annotate(request, bid, cid):
    '增加备注'
    m = Message()
    a = Annotation()
    a.chapter = Chapter.objects.get(id=cid)
    data = json.loads(request.body)
    row = readValue(data, 'row', m, '行号错误')
    if not m.ok:
        return HttpResponse(m, mimetype='application/json')
    a.row = int(row)
    start = readValue(data, 'start', m, '起始错误')
    if not m.ok:
        return HttpResponse(m, mimetype='application/json')
    a.start = int(start)
    end = readValue(data, 'end', m, '终止错误')
    if not m.ok:
        return HttpResponse(m, mimetype='application/json')
    a.end = int(end)
    style = readValue(data, 'style', m, '式样错误')
    if not m.ok:
        return HttpResponse(m, mimetype='application/json')
    a.style = style
    if 'context' in data:
        a.context = data['context']
    a.user = request.user
    ret = Annotation.annotate(a)
    if type(ret) == str:
        m.ok = False
        m.msg = ret
        return HttpResponse(m, mimetype='application/json')
    m.data = ret
    m.ok = True
    return HttpResponse(m, mimetype='application/json')

@login_required
@require_http_methods(["POST"])
def star(request, bid):
    '标星'
    book = Book.objects.get(id=bid)
    if not book.isStar(request.user):
        s = Star()
        s.book = book
        s.user = request.user
        s.save()
    return HttpResponse(book.stars.count())

@login_required
@require_http_methods(["POST"])
def unstar(request, bid):
    '取消标星'
    book = Book.objects.get(id=bid)
    if book.isStar(request.user):
        book.unstar(request.user)
    return HttpResponse(book.stars.count())

def get_dict(request, bid):
    '基本字典'
    book = Book.objects.get(id=bid)
    isStar = False
    if request.user.is_authenticated():
        isStar = book.isStar(request.user)
    return {
            'book': book,
            'isStar': isStar
            }

def book(request, bid):
    '书籍'
    context_dict = get_dict(request, bid)
    context = RequestContext(request, context_dict)
    return render_to_response('book.html', context)

def chapter(request, bid, cid):
    '章节'
    context_dict = get_dict(request, bid)
    c = Chapter.objects.get(id=cid)
    if bid != c.book.id:
        # TODO 书籍错误
        pass
    context_dict['chapter'] = c
    if request.user.is_authenticated():
        context_dict['lines'] = c.lines(request.user)
        context_dict['anns'] = c.anns(request.user)
    else:
        context_dict['lines'] = []
        context_dict['anns'] = []
    context = RequestContext(request, context_dict)
    return render_to_response('chapter.html', context)

def stargazers(request, bid):
    '关注的人'
    context_dict = get_dict(request, bid)
    stars = context_dict['book'].stars.all()
    context_dict['stars'] = stars
    context = RequestContext(request, context_dict)
    return render_to_response('stargazers.html', context)

def get_urls():
    return patterns('',
            url(r'^(?P<bid>\d+)$',
                book,
                name='book'),
            url(r'^(?P<bid>\d+)/(?P<cid>\d+)$',
                chapter,
                name='chapter'),
            url(r'^(?P<bid>\d+)/(?P<cid>\d+)/annotate$',
                annotate,
                name='annotate'),
            url(r'^(?P<bid>\d+)/star$',
                star,
                name='star'),
            url(r'^(?P<bid>\d+)/unstar$',
                unstar,
                name='unstar'),
            url(r'^(?P<bid>\d+)/stargazers$',
                stargazers,
                name='stargazers'),
            )

book_urls = (get_urls(), 'book', 'book')
