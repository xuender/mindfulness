# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User

from book import Book

class Pages(object):
    '翻页信息'
    def __init__(self, first=None, previous=None, next=None, end=None):
        '初始化'
        self.first = first
        self.previous = previous
        self.next = next
        self.end = end
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
    ps = None

    def pages(self):
        '获取翻页信息'
        if self.ps == None:
            cs = self.book.chapters.all()
            num = 0
            count = len(cs)
            for i in range(0, count):
                if cs[i].id == self.id:
                    num = i
            self.ps = Pages()
            if cs[0].id != self.id:
                self.ps.first = cs[0]
                self.ps.previous = cs[num - 1]
            if cs[count - 1].id != self.id:
                self.ps.end = cs[count - 1]
                self.ps.next = cs[num + 1]
        return self.ps

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
