from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from details.forms import Add_itemForm
from details.models import Item

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