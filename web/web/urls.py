from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from book import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'book.views.home', name='home'),
    url(r'^book/', include(views.book_urls)),
    url(r'^annotation$', 'book.views.annotation', name='annotation'),
    url(r'^demo$', 'book.views.demo', name='demo'),
    #url(r'^chapter/(?P<id>\d+)/annotate$', 'book.views.annotate', name='annotate'),

    #url(r'^accounts/logout/$', 'book.views.logout_view', name='logout'),
    url(r'^accounts/register/$', 'book.views.register', name='register'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
)
