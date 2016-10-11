from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.user_details, name='home'),
	url(r'^merchant/$', views.merchant_info, name='merchant'),
	url(r'^merchant/(?P<slug>[\w-]+)/$', views.merchant_details, name='info'),
	url(r'^location/(?P<slug>[\w-]+)/$', views.user_location, name='location'),
	url(r'^token/$', views.token_generator, name='token'),
	]