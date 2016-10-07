import string, random
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . models import Userdetails, Delivery, Merchant
from . forms import Add_detailsForm,Add_coordinatesForm, Add_merchantForm


# Create your views here.
def first_page(request):
	if request.method == "POST":
		form = Add_detailsForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	else:
		form = Add_detailsForm()
	return render(request, 'page_1.html', {'form':form})

def second_page(request, slug=None):
	user_info = get_object_or_404(Userdetails, slug=slug)
	form = Add_coordinatesForm(request.POST or None)
	form.fields['first_name'].initial = get_object_or_404(Userdetails, slug=slug).first_name
	form.fields['last_name'].initial = get_object_or_404(Userdetails, slug=slug).last_name
	form.fields['email'].initial = get_object_or_404(Userdetails, slug=slug).email

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

	return render(request, 'page_2.html',ctx)

def third_page(request, slug=None):
	info = get_object_or_404(Delivery, slug=slug)
	ctx = {}
	ctx['info']=info
	return render(request, 'page_3.html', ctx)

def fourth_page(request):

	def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	token = id_generator(7)
	ctx = {}
	ctx['token']=token
	return render(request, 'page_4.html', ctx)

def merchant(request):
	if request.method == "POST":
		form = Add_merchantForm(request.POST or None)
		if form.is_valid():
			instance = form.save()
			# instance = form.save(commit=False)
			# instance.save()
			return redirect('home')
	else:
		form = Add_merchantForm()
	return render(request, 'merchant.html', {'form':form})
