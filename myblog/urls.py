#coding:utf-8
from  django.conf.urls import url
from . import views
app_name='myblog'
urlpatterns=[

    url(r'^$',views.index,name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$',views.details,name="detail"),

]
