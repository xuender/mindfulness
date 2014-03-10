# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Book, Chapter
from django.template import RequestContext
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth import logout
from django.shortcuts import redirect

def home(request):
    t = get_template('home.html')
    html = t.render(RequestContext(request, {'books': Book.top()}))
    return HttpResponse(html)

def book(request, id):
    t = get_template('book.html')
    html = t.render(RequestContext(request, {'book': Book.objects.get(id=id)}))
    return HttpResponse(html)

def chapter(request, id):
    t = get_template('chapter.html')
    c = Chapter.objects.get(id=id)
    html = t.render(RequestContext(request,
        {'chapter': c, 'book': c.book}))
    return HttpResponse(html)

def logout_view(request):
    logout(request)
    return redirect('/')
