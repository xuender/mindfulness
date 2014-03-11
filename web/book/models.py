# -*- coding: utf-8 -*-
from django.db import models
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User
import re

class Book(UpdateModel):
    '图书'
    title = models.CharField(
            max_length=50,
            verbose_name='标题',
            )

    def __unicode__(self):
        return self.title

    @staticmethod
    def top(num=10):
        return Book.objects.all()[:num]

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'
        #ordering = ['status', '-visits', 'black']

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

    def __unicode__(self):
        return u'%s:%s'%(self.book, self.title)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = '章节'
        ordering = ['id']

class Star(UserModel):
    '星标'
    book=models.ForeignKey(Book,
            related_name='stars',
            verbose_name='图书'
            )

    def __unicode__(self):
        return u'%s:%s'%(self.book, self.create_by)

    class Meta:
        verbose_name = '星标'
        verbose_name_plural = '星标'
        ordering = ['-create_at']
        unique_together = ('create_by', 'book')

class Follow(UserModel):
    '关注'
    user=models.ForeignKey(User,
            related_name='followers',
            verbose_name='关注用户'
            )

    def __unicode__(self):
        return u'%s:%s'%(self.user, self.create_by)

    class Meta:
        verbose_name = '关注'
        verbose_name_plural = '关注'
        ordering = ['-create_at']
        unique_together = ('create_by', 'user')

class Annotation(UpdateModel):
    '批注'
    chapter=models.ForeignKey(Chapter,
            related_name='anotations',
            verbose_name='章节'
            )
    row=models.IntegerField(
            verbose_name='行号'
            )
    start=models.IntegerField(
            verbose_name='起始'
            )
    end=models.IntegerField(
            default=0,
            verbose_name='结束'
            )
    context=models.TextField(
            verbose_name='正文',
            )
    def _select(self):
        row = self.chapter.context.split('\n')[self.row - 1]
        regex = re.compile("(?x) (?: [\w-]+ | [\x80-\xff]{3} )")
        ret = regex.findall(row.encode('utf-8'))
        for i in ['，', '。']:
            while i in ret:
                ret.remove(i)
        return ret
    def select(self):
        '显示批注的目标内容'
        return ''.join(self._select()[self.start - 1 : self.end])

    def __unicode__(self):
        return u'%s:%s:%d'%(self.chapter, self.create_by, self.id)

    class Meta:
        verbose_name = '批注'
        verbose_name_plural = '批注'
        ordering = ['row', 'start']
