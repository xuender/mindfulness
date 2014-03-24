# -*- coding: utf-8 -*-
from django.db import models
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User

from book import Book

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
        app_label = 'book'
