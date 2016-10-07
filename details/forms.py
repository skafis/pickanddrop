from django import forms
from . models import Userdetails, Delivery, Merchant

class Add_detailsForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	telephone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Userdetails
		fields = [
			'first_name',
			'last_name',
			'email',
			'telephone',
			'country',
		]

class Add_coordinatesForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	amount = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Delivery
		fields = (
					'id',
					'first_name',
					'last_name',
					'email',
					'amount',
				)

class Add_merchantForm(forms.ModelForm):
	company = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	telephone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Merchant
		fields = [
		'company',
		'first_name',
		'last_name',
		'telephone',
		'location',
		]
