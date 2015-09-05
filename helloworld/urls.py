from django.conf.urls import include, url
from django.contrib import admin
from hello.views import hello, index

urlpatterns = [
    url(r'^$', index),
    url(r'^hello/$', hello),
]
