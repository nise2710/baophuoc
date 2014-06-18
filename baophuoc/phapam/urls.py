from django.conf.urls import patterns, url
from phapam import views

urlpatterns = patterns('',
    url(r'^(?P<cat_tag>\w+)$', views.phapam_index),
    url(r'^radio_chuabaophuoc/(?P<url_tag>\w+)$', views.phapam_radio),
    url(r'^phapthoai_hangngay/(?P<url_tag>\w+)$', views.phapam_phapthoai_hangngay),
    url(r'^phapthoai_chunhat/(?P<url_tag>\w+)$', views.phapam_phapthoai_chunhat),
    url(r'^phapthoai_batquantrai/(?P<url_tag>\w+)$', views.phapam_phapthoai_batquantrai),
)