# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from book.views import home, annotation
from book.models import Book, Chapter

class ViewTest(TestCase):
    '页面测试'
    def setUp(self):
        '初始化'
        self.factory = RequestFactory()
        self.anonymousUser = User(
                username='anonymousUser',
                first_name='Anonymous',
                last_name='User')
        self.user = User.objects.create_user(
                username='test',
                email='test@gmail.com',
                password='test')

    def test_get(self):
        '测试所有get访问页面'
        b = Book()
        b.title = '测试书籍'
        b.user = self.user
        b.save()
        c = Chapter()
        c.book = b
        c.title = '测试章节'
        c.context = '测试内容'
        c.user = self.user
        c.save()
        for p in ('/',
                '/annotation',
                '/book/1',
                '/book/1/1',
                '/book/1/stargazers'):
            response = self.client.get(p)
            self.assertEqual(response.status_code, 200, '无法访问 url:%s'%p)

    def test_home(self):
        '首页'
        request = self.factory.get('/')
        response = home(request)
        self.assertEqual(response.status_code, 200, '首页')

    def test_annotation(self):
        '首页'
        request = self.factory.get('/annotation')
        request.user = self.anonymousUser
        response = annotation(request)
        self.assertEqual(response.status_code, 200, '匿名')
        request.user = self.user
        response = annotation(request)
        self.assertEqual(response.status_code, 200, '用户')
