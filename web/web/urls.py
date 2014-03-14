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
    url(r'^starred/(?P<id>\d+)$', 'book.views.starred', name='starred'),
    url(r'^annotation$', 'book.views.annotation', name='annotation'),
    url(r'^accounts/logout/', 'book.views.logout_view', name='logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
)
