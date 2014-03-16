# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import json

class ComplexEncoder(json.JSONEncoder):
    '日期格式转换成JSON'
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)

class Message(object):
    '传输消息'
    ok = True
    def __str__(self):
        '转换成字符串'
        d = self.__dict__.copy()
        if 'data' in d and hasattr(d['data'], '__dict__'):
            temp = d['data'].__dict__
            d['data'] = {}
            for k in temp:
                if not hasattr(temp[k] , '__dict__'):
                    d['data'][k] = temp[k]
        return json.dumps(d, cls=ComplexEncoder)

class BaseModel(models.Model):
    '基础抽象实体'
    create_at=models.DateTimeField(
            default=datetime.now,
            help_text='本记录的创建时间',
            verbose_name='创建时间'
            )

    class Meta:
        abstract = True

class UserModel(BaseModel):
    '用户抽象实体'
    create_by=models.ForeignKey(User,
            verbose_name='创建人',
            related_name='+'
            )

    def update(self, *args, **kwargs):
        '保存时不修改时间'
        super(BaseModel, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        '保存时更修改时间'
        if hasattr(self, 'user'):
            print 'create user -- %s, id:%d'%(self.user, self.user.id)
            self.create_by = self.user
        super(BaseModel, self).save(*args, **kwargs)
    class Meta:
        abstract = True

class UpdateModel(UserModel):
    '修改抽象实体'
    modify_at=models.DateTimeField(
            default=datetime.now,
            verbose_name='修改时间',
            help_text='最后一次对本记录修改的时间'
            )
    modify_by=models.ForeignKey(User,
            verbose_name='修改人',
            related_name='+'
            )

    def save(self, *args, **kwargs):
        '保存时更修改时间'
        self.modify_at = datetime.now()
        if hasattr(self, 'user'):
            self.modify_by = self.user
            if not self.create_by_id:
                self.create_by = self.user
            print 'modify user -- %s, id:%d'%(self.user, self.user.id)
        super(UserModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
