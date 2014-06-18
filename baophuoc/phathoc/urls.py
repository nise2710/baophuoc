from django.conf.urls import patterns, url
from phathoc import views

urlpatterns = patterns('',
    url(r'^(?P<cat_tag>\w+)$', views.phathoc_index),
    url(r'^phathoccanban/(?P<url_tag>\w+)$', views.phathoc_canban),
    url(r'^phathocchuyensau/(?P<url_tag>\w+)$', views.phathoc_chuyensau),
    url(r'^phathocchotreem/(?P<url_tag>\w+)$', views.phathoc_chotreem),
    url(r'^thienhoc/(?P<url_tag>\w+)$', views.phathoc_thienhoc),
    url(r'^tinhdo/(?P<url_tag>\w+)$', views.phathoc_tinhdo),
    url(r'^mattong/(?P<url_tag>\w+)$', views.phathoc_mattong),
)