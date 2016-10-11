from django.shortcuts import render
from django.core.urlresolvers import reverse

import details.class_views.users as users 
import details.class_views.merchants as merchants

#customer
def user_details(request,template_name='user_registration.html'):
	return users.user_details(request,template_name=template_name)

def user_location(request,slug, template_name='user_location.html'):
	return users.user_location(request, slug, template_name=template_name)

def token_generator(request,template_name='token_generator.html'):
	return users.token_generator(request,template_name=template_name)

# Merchant
def merchant_info(request,template_name='merchant_info.html'):
	return merchants.merchant_info(request,template_name=template_name)

def merchant_details(request, slug, template_name='merchant_details.html'):
	return merchants.merchant_details(request, slug, template_name=template_name)



