from django.conf.urls import url

from . import views

urlpatterns = [
	# customer 
	url(r'^$', views.user_details, name='home'),
	url(r'^location/(?P<slug>[\w-]+)/$', views.user_location, name='location'),
	url(r'^token/$', views.token_generator, name='token'),

	# merchant
	url(r'^merchant/$', views.merchant_registaration, name='merchant'),
	url(r'^merchant/(?P<slug>[\w-]+)/$', views.merchant_details, name='info'),

	#merchant item_list
	url(r'^merchant/(?P<slug>[\w-]+)/item/$', views.add_items, name='item'),
	]