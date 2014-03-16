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

    def anns(self):
        return self.anotations.filter(style='a')

    def lines(self):
        return self.anotations.filter(~Q(style='a'))


    def __unicode__(self):
        return u'%s:%s'%(self.book, self.title)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
        ordering = ['id']
