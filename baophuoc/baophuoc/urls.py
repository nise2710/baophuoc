''' Filename: baophuoc.url.py '''
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    # apps
    url(r'trangchu/', include('trangchu.urls')),
    url(r'^thongtin/', include('thongtin.urls')), # connect to urls.py in app
    url(r'^phathoc/', include('phathoc.urls')),
    url(r'^phapam/', include('phapam.urls')),
    url(r'^thuvien/', include('thuvien.urls')),
    
    # plugins
    url(r'session_security/', include('session_security.urls')),  # session_security
    url(r'^ckeditor/', include('ckeditor.urls')),
    
    # others
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='trangchu/',permanent=False), name='index'), # redirect to /trangchu/
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}),
        (r'static/(?P<path>.*)','serve',{'document_root':settings.STATIC_ROOT}),
    )