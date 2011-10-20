from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('chametaxi.call.views',
    url(r'^callTaxi/$', 'callTaxi'),
    url(r'^checkTaxi/$', 'checkTaxi'),
    url(r'^listRides/$', 'listRides'),
    url(r'^acceptRide/$', 'acceptRide'),
)
