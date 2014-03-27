# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from common.models import UpdateModel, UserModel

from book import Book

class Follow(UserModel):
    '关注'
    user=models.ForeignKey(User,
            related_name='followers',
            verbose_name='关注用户'
            )
    book = models.ForeignKey(Book,
            related_name='followers',
            verbose_name='关注书籍'
            )

    def __unicode__(self):
        return u'%s:%s'%(self.user.first_name, self.create_by.first_name)

    class Meta:
        verbose_name = '关注'
        verbose_name_plural = '关注'
        ordering = ['-create_at']
        unique_together = ('create_by', 'user', 'book')
        app_label = 'book'
