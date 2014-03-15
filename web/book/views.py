# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Book, Chapter, Star
from django.template import RequestContext
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

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

def stargazers(request, id):
    '关注的人'
    book = Book.objects.get(id=id)
    stars = book.stars.all()
    context_dict = {
            'stars': stars,
            'book': book,
            'isStar': book.isStar(request.user),
            }
    context = RequestContext(request, context_dict)
    return render_to_response('stargazers.html', context)

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
@require_http_methods(["POST"])
def star(request, id):
    '标星'
    book = Book.objects.get(id=id)
    if not book.isStar(request.user):
        s = Star()
        s.book = book
        s.user = request.user
        s.save()
    return HttpResponse(book.stars.count())

@login_required
@require_http_methods(["POST"])
def unstar(request, id):
    '取消标星'
    book = Book.objects.get(id=id)
    if book.isStar(request.user):
        book.unstar(request.user)
    return HttpResponse(book.stars.count())
