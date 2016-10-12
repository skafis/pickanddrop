from django.shortcuts import render
from django.core.urlresolvers import reverse

import details.class_views.users as users 
import details.class_views.merchants as merchants
import details.class_views.item_list as item_list

#customer
def user_details(request,amount, template_name='user_registration.html'):
	return users.user_details(request, amount, template_name=template_name)
 
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

def view_items(request, template_name='view_items.html'):
	return item_list.view_items(request, template_name=template_name)

def view_items_details(request, pk, template_name='view_items_details.html'):
	return item_list.view_items_details(request, pk, template_name=template_name)

def register_user(request, pk, template_name='register_user.html'):
	return item_list.register_user(request, pk, template_name=template_name)

def get_user_location(request, pk, slug, template_name='get_user_location.html'):
	return item_list.get_user_location(request, pk, slug, template_name=template_name)