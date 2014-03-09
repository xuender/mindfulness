# -*- coding: utf-8 -*-
#import logging
#log = logging.getLogger('jp')
from django.contrib import admin

def register(model):
    '''
    标注 django admin @register class decorator, e.g.
    @register(Entry)
    class EntryAdmin(models.ModelAdmin):
        pass
    '''
    def inner(admin_cls):
        admin.site.register(model, admin_cls)
        return admin_cls
    return inner

class BaseAdmin(admin.ModelAdmin):
    '基础管理'
    def save_model( self, request, obj, form, change):
        '保存数据前设置user对象'
        obj.user = request.user
        obj.save()
