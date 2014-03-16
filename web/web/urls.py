from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'book.views.home', name='home'),
    url(r'^book/(?P<id>\d+)$', 'book.views.book', name='book'),
    url(r'^chapter/(?P<id>\d+)$', 'book.views.chapter', name='chapter'),
    url(r'^stargazers/(?P<id>\d+)$', 'book.views.stargazers', name='stargazers'),
    url(r'^star/(?P<id>\d+)$', 'book.views.star', name='star'),
    url(r'^unstar/(?P<id>\d+)$', 'book.views.unstar', name='unstar'),
    url(r'^annotation$', 'book.views.annotation', name='annotation'),
    url(r'^demo$', 'book.views.demo', name='demo'),
    url(r'^chapter/(?P<id>\d+)/annotate$', 'book.views.annotate', name='annotate'),

    url(r'^accounts/logout/', 'book.views.logout_view', name='logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
)
