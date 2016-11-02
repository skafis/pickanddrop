from django.forms import ModelForm
import django.forms as forms

class PesapalForm(forms.Form):
	#description=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	amount=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		fields=['amount','first_name','last_name','email',]
