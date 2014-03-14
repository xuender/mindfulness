# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Book, Chapter
from django.template import RequestContext
from django.contrib.auth import logout
from django.shortcuts import redirect, render_to_response

def home(request):
    context_dict = {'books': Book.top()}
    context = RequestContext(request, context_dict)
    return render_to_response('home.html', context)

def book(request, id):
    context_dict = {'book': Book.objects.get(id=id)}
    context = RequestContext(request, context_dict)
    return render_to_response('book.html', context)

def chapter(request, id):
    c = Chapter.objects.get(id=id)
    context_dict = {'chapter': c, 'book': c.book}
    context = RequestContext(request, context_dict)
    return render_to_response('chapter.html', context)

def annotation(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        return render_to_response('annotation.html', context)
    return render_to_response('registration/login_modal.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')
