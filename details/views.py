from django.shortcuts import render
from django.core.urlresolvers import reverse

import details.class_views.users as users 
import details.class_views.merchants as merchants
import details.class_views.item_list as item_list

#customer
def user_details(request,template_name='user_registration.html'):
	return users.user_details(request,template_name=template_name)
 
def user_location(request,slug, template_name='user_location.html'):
	return users.user_location(request, slug, template_name=template_name)

def token_generator(request,template_name='token_generator.html'):
	return users.token_generator(request,template_name=template_name)

# Merchant
def merchant_registaration(request,template_name='merchant_registration.html'):
	return merchants.merchant_registaration(request,template_name=template_name)

def merchant_details(request, slug, template_name='merchant_details.html'):
	return merchants.merchant_details(request, slug, template_name=template_name)

# Merchant item
def add_items(request, slug, template_name='add_item.html'):
	return item_list.add_items(request, slug,template_name=template_name)



