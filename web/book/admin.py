# -*- coding: UTF-8 -*-
from django.contrib import admin
from common import register, BaseAdmin
from models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = '雇员信息'
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = '用户扩展信息'

# Define a new User admin
@register(User)
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, EmployeeInline, )
#admin.site.register(User, UserAdmin)

class StarInline(admin.TabularInline):
    model = Star

@register(Book)
class BookAdmin(BaseAdmin):
    '图书管理'
    inlines = [StarInline,]
    search_fields = ['title']
    date_hierarchy = 'modify_at'
    #list_filter = ['query', 'num', ]
    list_display = ('title', 'create_by', 'create_at', 'modify_by', 'modify_at')
    readonly_fields = ('create_by', 'create_at', 'modify_by', 'modify_at')
    fieldsets = [
        (
            None,
            {'fields': ['title',]},
        ),
        (
            '其他',
            {
                'fields': ['create_by', 'create_at', 'modify_by', 'modify_at'],
                'classes': ['collapse'],
            },
        ),
    ]

@register(Chapter)
class ChapterAdmin(BaseAdmin):
    '章节管理'
    search_fields = ['title']
    date_hierarchy = 'modify_at'
    #list_filter = ['query', 'num', ]
    list_display = ('title', 'create_by', 'create_at', 'modify_by', 'modify_at')
    readonly_fields = ('create_by', 'create_at', 'modify_by', 'modify_at')
    fieldsets = [
        (
            None,
            {'fields': ['book', 'title', 'context']},
        ),
        (
            '其他',
            {
                'fields': ['create_by', 'create_at', 'modify_by', 'modify_at'],
                'classes': ['collapse'],
            },
        ),
    ]

#@register(Star)
#class StarAdmin(BaseAdmin):
#    '章节管理'
#    date_hierarchy = 'create_at'
#    #list_filter = ['query', 'num', ]
#    list_display = ('book', 'create_by', 'create_at')
#    readonly_fields = ('create_at',)
#    fieldsets = [
#        (
#            None,
#            {'fields': ['book', 'create_by', 'create_at']},
#        ),
#    ]
@register(Follow)
class FollowAdmin(BaseAdmin):
    '关注管理'
    date_hierarchy = 'create_at'
    #list_filter = ['query', 'num', ]
    list_display = ('user', 'create_by', 'create_at')
    readonly_fields = ('create_at',)
    fieldsets = [
        (
            None,
            {'fields': ['user', 'create_by', 'create_at']},
        ),
    ]
@register(Annotation)
class AnnotationAdmin(BaseAdmin):
    '批注管理'
    search_fields = ['context']
    date_hierarchy = 'modify_at'
    list_filter = ['chapter']
    list_display = ('chapter', 'row', 'start', 'end', 'style', 'create_by', 'create_at', 'modify_by', 'modify_at')
    readonly_fields = ('create_by', 'create_at', 'modify_by', 'modify_at')
    fieldsets = [
        (
            None,
            {'fields': ['chapter', 'row', 'start', 'end', 'style', 'context']},
        ),
        (
            '其他',
            {
                'fields': ['create_by', 'create_at', 'modify_by', 'modify_at'],
                'classes': ['collapse'],
            },
        ),
    ]
