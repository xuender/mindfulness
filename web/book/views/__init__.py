# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, url

from webs import home, logout_view, demo
from books import annotation
from books import book_urls
from accounts import logout_view, register
# 用户相关
from users import user_urls
