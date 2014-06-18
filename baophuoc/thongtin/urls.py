from django.conf.urls import patterns, url
from thongtin import views

urlpatterns = patterns('',
    url(r'^gioithieu$',views.thongtin_gioithieu_index),
    url(r'^gioithieu/(?P<url_tag>\w+)$', views.thongtin_gioithieu),
    url(r'^thongbao$',views.thongtin_thongbao_index),
    url(r'^thongbao/(?P<url_tag>\w+)$', views.thongtin_thongbao),
)