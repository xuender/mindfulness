#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(
            label="邮件",
            max_length=30,
            widget=forms.TextInput(
                attrs={'size': 30,}
                )
            )
    password = forms.CharField(
            label="密码",
            max_length=30,
            widget=forms.PasswordInput(
                attrs={'size': 20,}
                )
            )
    username = forms.CharField(
            label="昵称",
            max_length=30,
            widget=forms.TextInput(
                attrs={'size': 20,}
                )
            )

    def clean_username(self):
        '''验证重复昵称'''
        count = User.objects.filter(username__iexact=self.cleaned_data["username"]).count()
        if count == 0:
            return self.cleaned_data["username"]
        raise forms.ValidationError("该昵称已经被使用请使用其他的昵称")

    def clean_email(self):
        '''验证重复email'''
        count = User.objects.filter(email__iexact=self.cleaned_data["email"]).count()
        if count == 0:
            return self.cleaned_data["email"]
        raise forms.ValidationError("该邮箱已经被使用请使用其他的")
