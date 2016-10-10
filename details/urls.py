from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.first_page, name='home'),
	url(r'^merchant/$', views.merchant, name='merchant'),
	url(r'^merchant/(?P<slug>[\w-]+)/$', views.merchant_details, name='info'),
	url(r'^location/(?P<slug>[\w-]+)/$', views.second_page, name='location'),
	url(r'^payment/(?P<slug>[\w-]+)/$', views.third_page, name='payment'),
	url(r'^token/$', views.fourth_page, name='token'),
	]