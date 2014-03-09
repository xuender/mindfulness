# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Book, Chapter
from django.template import Context
from django.http import HttpResponse
from django.template.loader import get_template


def home(request):
    t = get_template('home.html')
    html = t.render(Context({'books': Book.top()}))
    return HttpResponse(html)

def book(request, id):
    t = get_template('book.html')
    html = t.render(Context({'book': Book.objects.get(id=id)}))
    return HttpResponse(html)

def chapter(request, id):
    t = get_template('chapter.html')
    html = t.render(Context({'chapter': Chapter.objects.get(id=id)}))
    return HttpResponse(html)
