# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User

from book import Book

class Chapter(UpdateModel):
    '章节'
    book=models.ForeignKey(Book,
            related_name='chapters',
            verbose_name='图书'
            )
    title=models.CharField(
            max_length=50,
            verbose_name='标题',
            )
    context=models.TextField(
            verbose_name='正文',
            )

    def anns(self, user):
        return self.annotations.filter(style='a', create_by=user)

    def lines(self, user):
        return self.annotations.filter(~Q(style='a'), create_by=user)

    def ann_count(self, user):
        '某用户的批注数量'
        return self.annotations.filter(create_by=user).count()


    def __unicode__(self):
        return u'%s:%s'%(self.book, self.title)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
        ordering = ['id']
        app_label = 'book'
