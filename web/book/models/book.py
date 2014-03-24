# -*- coding: utf-8 -*-
from django.db import models
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User

class Book(UpdateModel):
    '图书'
    title = models.CharField(
            max_length=50,
            verbose_name='标题',
            )
    def isStar(self, user):
        '用户是否关注'
        return self.stars.filter(create_by=user).count() > 0

    def unstar(self, user):
        '取消用户关注'
        self.stars.filter(create_by=user).delete()

    def __unicode__(self):
        return self.title

    @staticmethod
    def top(num=10):
        return Book.objects.all()[:num]

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'
        app_label = 'book'
        #ordering = ['status', '-visits', 'black']
