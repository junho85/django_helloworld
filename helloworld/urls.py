from django.conf.urls import include, url
from django.contrib import admin
from hello.views import hello, index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
]
