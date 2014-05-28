from django.conf.urls import patterns, url
from trangchu import views

urlpatterns = patterns('',
    url(r'^$',views.trangchu_index, name='trangchu_index'),
)