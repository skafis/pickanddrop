from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from details.forms import Add_itemForm, Add_detailsForm, Add_coordinatesForm
from details.models import Item, Userdetails, Delivery, Merchant

def add_items(request, slug,template_name='add_item.html'):
	ctx = {}
	if request.method == "POST":
		form = Add_itemForm(request.POST or None)
		form.fields['merchant'].initial = Merchant.objects.get(slug=slug).company
		if form.is_valid():
			# instance = form.save()
			form.save()
			return redirect ('/')
	else:
		form = Add_itemForm()
	ctx['form'] = form
	return render(request, template_name, ctx)

def view_items(request, template_name='view_items.html'):
	items = Item.objects.order_by('-id')
	ctx = {}
	ctx['items']= items
	return render(request, template_name, ctx)

# def view_items_details(request, pk, template_name='view_items_details.html'):
# 	item = Item.objects.get(pk=pk)
# 	ctx = {}
# 	ctx['item']= item
# 	ctx['amount']= int(item.cost)
# 	return render(request, template_name, ctx)

def register_user(request, pk, template_name='register_user.html'):
	if request.method == "POST":
		form = Add_detailsForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			# pk = request.POST['pk']
			slug = request.POST['slug']
			return redirect('user_location')
			# return HttpResponseRedirect(instance.get_absolute_url())
	else:
		form = Add_detailsForm()

	ctx = {}
	ctx['form']=form
	return render(request, template_name, ctx)

def get_user_location(request, pk, slug=None, template_name='get_user_location.html'):
	# user_info = Userdetails.objects.get(slug=slug)
	form = Add_coordinatesForm(request.POST or None)
	form.fields['first_name'].initial = Userdetails.objects.get(slug=slug).first_name
	form.fields['last_name'].initial = Userdetails.objects.get(slug=slug).last_name
	form.fields['email'].initial = Userdetails.objects.get(slug=slug).email

	ctx = {}
	ctx['form']=form

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		description='none'
		types='MERCHANT'
		reference='none'
		return redirect('http://192.168.0.13/pickanddrop/pesapal-iframe.php?first_name=%s&last_name=%s&amount=%s&email=%s&description=%s&type=%s&reference=%s'%(request.POST['first_name'], 
			request.POST['last_name'], request.POST['amount'], request.POST['email'],description,types,reference))

	return render(request, template_name, ctx)
