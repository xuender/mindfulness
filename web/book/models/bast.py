#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 ender xu <xuender@gmail.com>
#
# Distributed under terms of the MIT license.
from django.db import models
from django.contrib.auth.models import User

from common.models import UserModel

from book import Book

class Bast(UserModel):
    '推荐'
    book = models.ForeignKey(Book,
            related_name = 'basts',
            verbose_name = '推荐'
            )
    author = models.ForeignKey(User,
            verbose_name='作者',
            related_name='basts'
            )
    def __unicode__(self):
        return u'%s:%s'%(self.author.first_name, self.book)

    class Meta:
        verbose_name = '推荐'
        verbose_name_plural = '推荐'
        ordering = ['-create_at']
        unique_together = ('book', 'author')
        app_label = 'book'
