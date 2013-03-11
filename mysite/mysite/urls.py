from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from mysite.views import current_datetime, current_datetime_temp, hours_ahead, hours_ahead_temp, form_get
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    (r'^time/$', current_datetime_temp),
    (r'^time/plus/(\d{1,2})/$', hours_ahead_temp),
    (r'^form', form_get),
    (r'^static$', 'static.html'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
