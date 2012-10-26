from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^login/$', 'evernotoy.views.login'),
    ('^home/$', 'evernotoy.views.home'),
    ('^load_more/(\d+)/(\d+)/$', 'evernotoy.views.load_more'),
    ('^logout/$', 'evernotoy.views.logout'),
    ('^$', redirect_to, {'url': '/home/'}),
)
