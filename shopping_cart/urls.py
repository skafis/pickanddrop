from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^update/(?P<pk>\d+)/$',views.update_cart, name='update_cart'),
	url(r'^view_cart/$',views.view_cart, name='view_cart'),
	# url(r'^checkout/(?P<amount>\d+)/$',views.checkout, name='checkout'),
	]
