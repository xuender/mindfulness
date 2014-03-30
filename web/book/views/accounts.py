# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods

from book.forms import RegisterForm
from book.help import getCG

def logout_view(request):
    '退出'
    logout(request)
    return redirect('/')

@require_http_methods(["POST", 'GET'])
def register(request):
    '注册'
    print '注册'
    if request.method=="POST":
        form=RegisterForm(request.POST.copy())
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(email ,email,password)
            user.first_name = username
            user.groups.add(getCG())
            user.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('/')
    context_dict = {'form': RegisterForm()}
    context = RequestContext(request, context_dict)
    return render_to_response('registration/register.html', context)
