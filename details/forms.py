import itertools
from django import forms
from django.utils.text import slugify

from . models import Userdetails, Delivery, Merchant, Item

class Add_detailsForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	telephone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	amount = forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control'}))
	class Meta:
		model = Userdetails
		fields = [
			'first_name',
			'last_name',
			'email',
			'telephone',
			'country',
			'amount',
		]

class Add_coordinatesForm(forms.ModelForm):
	# first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	# last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	# email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Delivery
		fields = (
					'id',
					# 'first_name',
					# 'last_name',
					# 'email',
					'amount',
				)

class Add_merchantForm(forms.ModelForm):
	company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	telephone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Merchant
		fields = [
		'company',
		'first_name',
		'last_name',
		'email',
		'telephone',
		'location',
		]

	def save(self):
		instance = super(Add_merchantForm, self).save(commit=False)

		max_length = Merchant._meta.get_field('slug').max_length
		instance.slug = orig = slugify(instance.company)[:max_length]

		for x in itertools.count(1):
			if not Merchant.objects.filter(slug=instance.slug).exists():
				break

			# Truncate the original slug dynamically. Minus 1 for the hyphen.
			instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

		instance.save()

		return instance

class Add_itemForm(forms.ModelForm):
		# name = forms.ModelChoiceField(queryset=Merchant.objects.get('company').order_by('id'),widget=forms.Select(attrs={'class':'form-control selectpicker','data-live-search' : "true"}))	
		# name = forms.ModelChoiceField(queryset=Merchant.objects.get(slug=slug).company,widget=forms.TextInput(attrs={'class':'form-control'}))
		merchant = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
		item_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
		cost = forms.DecimalField(widget=forms.TextInput(attrs={'class':'form-control'}))
		class Meta:
			model = Item
			fields = ['merchant','item_name','cost']
