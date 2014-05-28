''' Filename: baophuoc.url.py '''
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'baophuoc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'trangchu/', include('trangchu.urls')),
    url(r'^$', RedirectView.as_view(url='trangchu/',permanent=False), name='index'), # redirect to /trangchu/
    url(r'^thongtin/', include('thongtin.urls')), # connect to urls.py in rango app
    (r'^ckeditor/', include('ckeditor.urls')),  
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}),
        (r'static/(?P<path>.*)','serve',{'document_root':settings.STATIC_ROOT}),
    )