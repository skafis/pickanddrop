from django.conf.urls import url

from . import views

urlpatterns = [
	# customer 
	url(r'^(?P<amount>\d+)/$', views.user_details, name='home'),
	# url(r'^location/(?P<slug>[\w-]+)/$', views.user_location, name='location'),
	url(r'^location/(?P<slug>[\w-]+)/$', views.user_location, name='location'),
	url(r'^token/$', views.token_generator, name='token'),

	# merchant
	url(r'^merchant/$', views.merchant_registaration, name='merchant'),
	url(r'^info/(?P<slug>[\w-]+)/$', views.merchant_details, name='info'),

	#merchant item_listslug
	url(r'^info/(?P<slug>[\w-]+)/item/$', views.add_items, name='item'),
	url(r'^$', views.view_items, name='view'),
	# url(r'^views/(?P<pk>\d+)/$', views.view_items_details, name='views'),
	]
