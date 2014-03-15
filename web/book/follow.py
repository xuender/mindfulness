# -*- coding: utf-8 -*-
from django.db import models
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User

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
