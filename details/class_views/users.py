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
			form.save()
			# return HttpResponseRedirect(instance.get_absolute_url())
			return redirect("/location/%s" % str(request.POST['first_name']).lower())
	#else:
		#form = Add_detailsForm()
	return render(request, template_name, ctx)

def user_location(request, slug, template_name='user_location.html'):
	try:
		ctx = {}
		user_info = Userdetails.objects.get(slug=slug)
		form = Add_coordinatesForm(request.POST or None)
		form.fields['first_name'].initial = Userdetails.objects.get(slug=slug).first_name
		form.fields['last_name'].initial = Userdetails.objects.get(slug=slug).last_name
		form.fields['email'].initial = Userdetails.objects.get(slug=slug).email
		ctx['form']=form

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			description='none'
			types='MERCHANT'
			reference='none'
			total_amount = float(user_info.amount) + float(request.POST['amount'])
			return redirect('http://45.55.252.17/pickanddrop/pesapal-iframe.php?first_name=%s&last_name=%s&amount=%s&email=%s&description=%s&type=%s&reference=%s'%(request.POST['first_name'], 
				request.POST['last_name'], total_amount, request.POST['email'],description,types,reference))
	except:
		raise 

	return render(request, template_name, ctx)

def token_generator(request, template_name='token_generator.html'):

	def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	token = id_generator(7)
	ctx = {}
	ctx['token']=token
	return render(request, template_name, ctx)
