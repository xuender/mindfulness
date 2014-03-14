# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Book, Chapter, Star
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.decorators import login_required

def home(request):
    '首页'
    context_dict = {'books': Book.top()}
    context = RequestContext(request, context_dict)
    return render_to_response('home.html', context)

def book(request, id):
    '书籍'
    book = Book.objects.get(id=id)
    context_dict = {
            'book': book,
            'isStar': book.isStar(request.user),
            }
    context = RequestContext(request, context_dict)
    return render_to_response('book.html', context)

def chapter(request, id):
    '章节'
    c = Chapter.objects.get(id=id)
    context_dict = {
            'chapter': c,
            'book': c.book,
            'isStar': c.book.isStar(request.user),
            }
    context = RequestContext(request, context_dict)
    return render_to_response('chapter.html', context)

def annotation(request):
    '显示标注弹出窗口'
    context = RequestContext(request)
    if request.user.is_authenticated():
        return render_to_response('annotation.html', context)
    return render_to_response('registration/login_modal.html', context)

def logout_view(request):
    '退出'
    logout(request)
    return redirect('/')

@login_required
def starred(request, id):
    '标星'
    book = Book.objects.get(id=id)
    if book.isStar(request.user):
        return HttpResponse(0)
    else:
        s = Star()
        s.book = book
        s.user = request.user
        s.save()
        return HttpResponse(book.stars.count())
