''' thongtin.url.py '''
from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from thongtin import views

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='gioithieu/chuabaophuoc',permanent=False), name='thongtin'),
    url(r'^gioithieu/(?P<url_tag>\w+)$', views.thongtin_gioithieu),
    url(r'^thongbao/(?P<url_tag>\w+)$', views.thongtin_thongbao),
	url(r'^(?P<url_tag>\w+)$', views.thongtin_tonchi),
)

