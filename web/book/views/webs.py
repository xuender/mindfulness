# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from common.models import Message
from book.models import Book

def home(request):
    '首页'
    context_dict = {'books': Book.top()}
    context = RequestContext(request, context_dict)
    return render_to_response('home.html', context)

def logout_view(request):
    '退出'
    logout(request)
    return redirect('/')

def demo(request):
    data = serializers.serialize('json', Book.objects.all())
    return HttpResponse(data, mimetype='application/json')
