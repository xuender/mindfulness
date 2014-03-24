# -*- coding: utf-8 -*-
from django.db import models
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '用户信息'
    user = models.OneToOneField(User,
            primary_key=True,
            parent_link=True
            )
    note = models.TextField(
            blank=True, null=True,
            verbose_name='备注',
            )
    def __unicode__(self):
        return self.user.username

class Employee(models.Model):
    '雇员信息'
    user = models.OneToOneField(User,
            primary_key=True,
            parent_link=True
            )
    tel = models.CharField(
            blank=True, null=True,
            max_length=20,
            verbose_name='电话',
            )
    def __unicode__(self):
        return self.user.username
