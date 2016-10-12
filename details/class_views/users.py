import string, random
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from details.models import Userdetails, Delivery, Item
from details.forms import Add_detailsForm,Add_coordinatesForm


# Create your views here.
def user_details(request, amount, template_name='user_registration.html'):
	form = Add_detailsForm(request.POST or None)
	ctx = {}
	ctx['form']=form
	form.fields['amount'].initial = amount

	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
	#else:
		#form = Add_detailsForm()
	return render(request, template_name, ctx)

def user_location(request, slug=None, template_name='user_location.html'):
	user_info = get_object_or_404(Userdetails, slug=slug)
	# points = Merchant.objects.all()
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
		total_amount = float(user_info.amount) + float(request.POST['amount'])
		return redirect('http://192.168.0.13/pickanddrop/pesapal-iframe.php?first_name=%s&last_name=%s&amount=%s&email=%s&description=%s&type=%s&reference=%s'%(request.POST['first_name'], 
			request.POST['last_name'], total_amount, request.POST['email'],description,types,reference))

	return render(request, template_name, ctx)

def token_generator(request, template_name='token_generator.html'):

	def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	token = id_generator(7)
	ctx = {}
	ctx['token']=token
	return render(request, template_name, ctx)