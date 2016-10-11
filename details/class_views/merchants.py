from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from details.forms import Add_merchantForm
from details.models import Merchant

def merchant_info(request,template_name='merchant_info.html'):
	if request.method == "POST":
		form = Add_merchantForm(request.POST or None)
		if form.is_valid():
			instance = form.save()
			# instance = form.save(commit=False)
			# instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	else:
		form = Add_merchantForm()
	ctx = {}
	ctx['form'] = form
	return render(request, template_name, ctx)

def merchant_details(request, slug=None, template_name='me.html'):
	info  = get_object_or_404(Merchant, slug=slug)
	ctx = {}
	ctx['info'] = info
	
	return render(request, template_name, ctx)
