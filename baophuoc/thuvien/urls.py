from django.conf.urls import patterns, url
from thuvien import views

urlpatterns = patterns('',
    url(r'^hinhanh$', views.thuvien_photo_index),
    url(r'^video$', views.thuvien_video_index),
    url(r'^hinhanh/(?P<url_tag>\w+)$', views.thuvien_photo),
    url(r'^video/(?P<url_tag>\w+)$', views.thuvien_video),
)