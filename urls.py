from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$',
                        'django.views.static.serve',
                        {'document_root': 'static'}),
                       (r'^$',
                        'django.views.generic.simple.direct_to_template',
                        {'template' : 'home.html'}),
                       (r'^about$',
                        'django.views.generic.simple.direct_to_template',
                        {'template' : 'about.html'}),
                       (r'^contact$',
                        'django.views.generic.simple.direct_to_template',
                        {'template' : 'contact.html'}),
                       )
