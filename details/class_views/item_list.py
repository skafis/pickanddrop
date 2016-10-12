from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from details.forms import Add_itemForm, Add_detailsForm
from details.models import Item, Userdetails

def add_items(request, slug,template_name='add_item.html'):
	if request.method == "POST":
		form = Add_itemForm(request.POST or None)
		if form.is_valid():
			# instance = form.save()
			form.save()
			return redirect ('home')
	else:
		form = Add_itemForm()
	ctx = {}
	ctx['form'] = form
	return render(request, template_name, ctx)

def view_items(request, template_name='view_items.html'):
	items = Item.objects.order_by('-id')
	ctx = {}
	ctx['items']= items
	return render(request, template_name, ctx)

def view_items_details(request, pk, template_name='view_items_details.html'):
	item = Item.objects.get(pk=pk)
	ctx = {}
	ctx['item']= item
	return render(request, template_name, ctx)

def register_user(request, pk, template_name='register_user.html'):
	if request.method == "POST":
		form = Add_detailsForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	else:
		form = Add_detailsForm()

	ctx = {}
	ctx['form']=form
	return render(request, template_name, ctx)