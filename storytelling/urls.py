from django.conf.urls import patterns, include, url
from django.contrib import admin
from pdf.views import *
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storytelling.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^enter/', AccessCodeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^book/(?P<book_id>[0-9]+)/', 'pdf.views.book_detail', name='book_detail'),
    url(r'^console/$', 'pdf.views.console', name='console'),
    url(r'^$', lambda x: HttpResponseRedirect('/enter/')),
)
