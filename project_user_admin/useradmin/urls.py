from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from userinfo.models import UserInfo
from userinfo.views import UserInfoCreate, UserInfoUpdate, UserInfoDelete, UserInfoList, GreetingView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'useradmin.views.home', name='home'),
    # url(r'^useradmin/', include('useradmin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 
    # 	ListView.as_view(
    # 		queryset=UserInfo.objects.all(),
    # 		template_name="user_list.html"),
    # 	name='index'),

    url(r'^$', UserInfoList.as_view(), name="index"),
    url(r'^add/$', UserInfoCreate.as_view(), name="user_add"),
    url(r'^edit/(?P<pk>\d+)$', UserInfoUpdate.as_view(), name="user_edit"),
    url(r'^delete/(?P<pk>\d+)$', UserInfoDelete.as_view(), name="user_add"),

    url(r'^greet', GreetingView.as_view())
)
